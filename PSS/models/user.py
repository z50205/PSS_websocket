from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from PSS import db,login_manager
from flask_login import UserMixin
from hashlib import md5

class User(UserMixin,db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(64),unique=True,index=True)
    email=db.Column(db.String(64),unique=True,index=True)
    password_hash=db.Column(db.String(128))
    about_me=db.Column(db.String(128))
    create_time=db.Column(db.DateTime,default=datetime.utcnow)
    is_activated=db.Column(db.Boolean,default=False)

    def __repr__(self):
        return 'id={},username={},email={},password_hash={}'.format(
            self.id,self.username,self.email,self.password_hash
        )
    
    def avatar(self,size=80):
        md5_digest=md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://gravatar.com/avatar/{}?d=identicon&s={}'.format(md5_digest,size)
    
    def set_password(self,password):
        self.password_hash=generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))