from commen.db import db
from sqlalchemy import String, Integer, Boolean, Column, DateTime, BigInteger
from werkzeug.security import generate_password_hash, check_password_hash


class UserModel(db.Model):
    """
     Model for user management
     +++++++++++++++++++++++++
    """
    __tablename__ = 'users'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    username = Column(String(100), nullable=False, index=True, unique=True)
    first_name = Column(String(32), nullable=False)
    last_name = Column(String(32), nullable=False)
    email = Column(String(100), unique=True, index=True)
    password_hash = Column(String(100))
    phone_number = Column(String(10), nullable=True)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=db.func.now(), onupdate=db.func.now())
    updated_at = Column(DateTime(timezone=True), default=db.func.now(), onupdate=db.func.now())

    def __init__(self, username, first_name, last_name, email, password, phone_number, is_active, is_admin):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password_hash = self.set_password(password)
        self.phone_number = phone_number
        self.is_active = is_active
        self.is_admin = is_admin


    def set_password(self, password):
        return generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        """Represent instance as a unique string."""
        return '<User({username!r})>'.format(username=self.username)

