from flask import render_template, request, redirect, url_for, session, flash
from app import app, db
from app.models import Comment
from sqlalchemy.exc import SQLAlchemyError

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'username' in session:
        return redirect(url_for('comments'))
    
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        if username:
            session['username'] = username
            return redirect(url_for('comments'))
        else:
            flash('Username cannot be empty', 'error')
    return render_template('index.html')

@app.route('/comments', methods=['GET', 'POST'])
def comments():
    if 'username' not in session:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        text = request.form.get('content', '').strip()
        if text:
            try:
                new_comment = Comment(username=session['username'], text=text)
                db.session.add(new_comment)
                db.session.commit()
            except SQLAlchemyError as e:
                db.session.rollback()
                app.logger.error(f"Database error: {str(e)}")
        else:
            flash('Comment cannot be empty', 'error')
        return redirect(url_for('comments'))
    
    try:
        all_comments = Comment.query.order_by(Comment.timestamp.desc()).with_entities(Comment.id, Comment.username, Comment.text).all()
    except SQLAlchemyError as e:
        flash('An error occurred while fetching comments', 'error')
        app.logger.error(f"Database error: {str(e)}")
        all_comments = []
    
    return render_template('comments.html', comments=all_comments)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/delete_comment/<int:comment_id>', methods=['POST'])
def delete_comment(comment_id):
    if 'username' not in session or session['username'] != 'admin':
        flash('You do not have permission to delete comments', 'error')
        return redirect(url_for('comments'))
    
    try:
        comment = Comment.query.get(comment_id)
        if comment:
            db.session.delete(comment)
            db.session.commit()
            flash('Comment deleted successfully', 'success')
        else:
            flash('Comment not found', 'error')
    except SQLAlchemyError as e:
        db.session.rollback()
        flash('An error occurred while deleting the comment', 'error')
        app.logger.error(f"Database error: {str(e)}")

    return redirect(url_for('comments'))
