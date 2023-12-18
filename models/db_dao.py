from copy import copy

from models.admin_dao import AdminDao
from models.db_dao import Db as db
from models.user_dao import UserDao
from models.book_dao import BookDao

class DbDao(db):
    def __init__(self, app):
        super(DbDao, self).__init__(app)
        
        self.book = BookDao(copy(self))
        self.user = UserDao(copy(self))
        self.admin = AdminDao(copy(self))