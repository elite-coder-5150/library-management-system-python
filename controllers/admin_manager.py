from app.admin import Admin

class AdminManager():
    def __init__(self, Dao):
        self.admin = Admin(Dao.db.admin)
        self.user = Dao.db.user
        self.dao = self.admin.dao
        
    def register(self, email, password):
        admin = self.dao.get_by_email(email)
        
        if admin is not None:
            return False
        
        admin_pass = admin['password']
        
        if admin_pass != password:
            return False
        
    def get(self, id):
        admin = self.dao.get_by_id(id)
        return admin
    
    def get_users_list(self):
        admin = self.user.list()
        print(admin)
        return admin
    
    def logout(self):
        self.admin.logout()
        
    def user_list(self):
        return self.user.list()
    