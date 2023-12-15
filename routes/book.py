from flask import Blueprint, g, escape, session, redirect, render_template, request, jsonify, Response, flash
from app import Dao

from controllers.user_manager import UserManager
from controllers.book_manager import BookManager

book_view = Blueprint('book_routes', __name__,  template_folder='/templates')
book_manager = BookManager(Dao)
user_manager = UserManager(Dao)

@book_view.route('/books', default={'id': None})
@book_view.route('/books/<int:id>')
def home(id):
    user_manager.user.set_session(session, g)
    
    if id != None:
        b = book_manager.get_book(id)
        
        print('--------------------------------')
        print(b)
        
        user_books = {}
        
        if user_manager.user.is_logged_in():
            user_books = book_manager.get_reserved_books_by_user(user_id=user_manager.uid())['user_books'].split(', ')
            
        if b and len(b) < 1:
            return render_template('book_view.html', error="nno bok found")
        
        return render_template('book_view.html', books=b, g=g, user_books=user_books)
    
    else:
        b = book_manager._list()
        user_books = []
         
        if user_manager.user.is_logged_in():
            reserved_books = book_manager.get_reserved_books_by_user(user_id=user_manager.user.uid())
             
            if reserved_books is not None:
                 user_books = reserved_books['user_books'].split(',')
                 
                 
        print('--------------------------------')
        print(user_books)
        
        if b and len(b) < 1:
            return render_template('books.html', error="no books found")
        return render_template('books.html', books=b, g=g,  user_books=user_books)
    return render_template('books.html', books=b, g=g)

@book_view.route('/books/add/<id>', method=['GET'])
@user_manager.user.login_required
def add(id):
    user_id = user_manager.user.uid()
    book_manager.reserve_book(user_id, id)
    
    b = book_manager._list()
    user_manager.set_session(session, g)
    
    return render_template('books.html', msg="book reserved", books=b, g=g)

@book_view.route('books/search', method=['GET'])
def search():
    user_manager.user.set_session(session, g)
    
    if "keyword" not in request.args:
        return render_template("search.html")
    
    keyword = request.args['keyword']
    
    if len(keyword) < 1:
        return redirect('/books')
    
    d = book_manager.search(keyword)
    
    if len(d) > 0:
        return render_template("books.html", serach=True, books=d, count=len(d), keyword=escape(keyword), g = g)
    return render_template("books.html", error="no books found", keywords=escape(keyword))