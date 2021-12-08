from enum import unique
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
    
class Products(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(150), unique = False)
    price=db.Column(db.Integer, unique=False)
    name=db.Column(db.String(50), unique = False)
    image=db.Column(db.String(500), unique = False)
    category=db.Column(db.String(20), unique = False)
    
    def __repr__(self):
        return f"User('{self.name}', '{self.price}')"

    