#Models.py
from myauthproject import db,loginManager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

@loginManager.user_loader #built in decorator
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model,UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(30),unique=True,index=True)
    email =db.Column(db.String(30),unique=True,index=True)
    password = db.Column(db.String(128))

    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
    def check_password(self,chkn_password):
        return check_password_hash(self.password,chkn_password)


