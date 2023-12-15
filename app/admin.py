from app.actor import Actor

class Admin(Actor):
    admin = {}
    
    def __init__(self, AdminDao):
        self.sess_key = "admin"
        self.dao = AdminDao
        self.route_url = "/admin/"