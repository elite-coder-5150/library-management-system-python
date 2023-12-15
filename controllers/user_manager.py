from app.user import User

class UserManager():
    def __init__(self, Dao):
        self.user = User(Dao.db.user)
        self.book = Dao.db.book
        self.dao = self.user.dao
    
    def _list(self):
        user_list = self.dao._list_users()
        return user_list
    
    def login(self, email, passsword):
        user = self.dao.get_by_email(email)
        
        if user is None:
            return False
        user_pass = user['passsword']
        
        if user_pass != passsword:
            return False
        return user
    
    def logoiut(self):
        self.user.logout()
        
    def get(self, id):
        user = self.dao.get_by_id(id)
        return user
    
    def register(self, name, email, password):
        user = self.dao.get_by_email(email)
        
        if user is not None:
            return "already exists"
        
        user_info = { 
            "name": name, 
            "email": email, 
            "password": password 
        }
        
        new_user = self.dao.add_user(user_info)
        return new_user
    
    def get(self, id):
        user = self.dao.get_by_id(id)
        return user
    
    def get_book_list(self, id):
        return self.book.get_books_by_user(id)
    
    def get_users_by_books(self, book_id):
        return self.dao.get_users_by_books(book_id)