from models.db_dao import DbDao

class Dao():
    def __init__(self, app):
        self.db = DbDao(app)