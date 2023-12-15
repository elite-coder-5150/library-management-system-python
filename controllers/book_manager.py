from app.books import Book

class BookManager():
    def __init__(self, Dao):
        self.misc = Book(Dao.db.book)
        self.dao = self.misc.dao
        
    def _list(self, availability=1, user_id=None):
        if user_id is not None:
            book_list = self.dao.list_by_user(user_id)
            
        else:
            book_list = self.dao.list(availability)
        
        return book_list
    
    def get_reserved_books_by_user(self, user_id):
        books = self.dao.get_reserved_books_by_user(user_id)
        return books
    
    def get_book(self, id):
        books = self.dao.get_book(id)
        return books
    
    def search(self, keyword, availability=1):
        books = self.dao.search(keyword, availability)
        return books
    
    def reserve(self, user_id, book_id):
        books = self.dao.reserve(user_id, book_id)
        return books
    
    def get_user_books(self, user_id):
        books = self.dao.get_books_by_user(user_id)
        
    def get_user_book_count(self, user_id):
        books = self.dao.get_books_by_user(user_id)
        return books
    
    def delete(self, id):
        self.dao.delete_book(id)