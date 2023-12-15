from functools import wraps
from flask import g, request, redirect, session

class Actor():
    sess_key = ''
    route_url = '/'
    
    def uid(self):
        if self.is_logged_in():
            return session[self.sess_key]
        
        return "err"
    
    def set_session(self, sessiong, g):
        g.user = 0
        
        if self.is_logged_in():
            g.user = sessiong[self.sess_key]
    
    def is_logged_in(self):
        if self.sess_key in session and session[self.sess_key] and session[self.sess_key] > 0:
            return True
        
        return False
    
    def login_required(self, f, path="signin"):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if self.sess_key in session and session[self.sess_key] is None:
                print(path)
                return redirect(self.route_url + path)
            return f(*args, **kwargs)
        return decorated_function
    
    
    def redirect_if_login(self, f, path="/"):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if self.sess_key in session and session[self.sess_key] is not None:
                return redirect(self.route_url + path)
            return f(*args, **kwargs)
        return decorated_function
    
    def logout(self):
        session[self.sess_key] = None
        
    
    def login(self):
        pass