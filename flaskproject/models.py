from flaskproject import db

class UserDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique = False)
    email = db.Column(db.String(120), unique = False)
    password = db.Column(db.String(120), unique = False)
    
    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class Admins(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique = False)
    email = db.Column(db.String(120), unique = False)
    password = db.Column(db.String(120), unique = False)
    
    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

