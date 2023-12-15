from app.actor import Actor

class User(Actor):
    id = 0
    name = ""
    local = False
    user = {}
    
    def __init__(self, UserDao):
        self.dao = UserDao
        self.sess_key = "user" #session key