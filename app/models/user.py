from . import db, bcrypt
# from app import ma
import datetime
import enum

class User(db.Model):
    class Role(enum.Enum):
        """
        Role of a user in the system.
        """
        admin = 'admin'
        moderator = 'moderator'
        viewer = 'viewer'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(191), nullable=False, unique=True)
    username = db.Column(db.String(191), nullable=False, unique=True)
    fullname = db.Column(db.String(191), nullable=True)
    status = db.Column(db.Integer, default=1)
    password_hash = db.Column(db.String(100))
    id_token = db.Column(db.String(512), nullable=True)
    image = db.Column(db.Text(), nullable=True)
    role = db.Column(db.Enum(Role), nullable=True, default=Role.viewer)
    last_login = db.Column(db.TIMESTAMP, default=datetime.datetime.now)


    def to_dict(self):
        return {
            'username': self.username,
            'email': self.email,
            'fullname': self.fullname,
            'status': self.status,
            'password_hash': self.password_hash,
            'id_token': self.id_token,
            'image': self.image,
        }


    # def password(self, password):
    #     self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

