from sqlalchemy import BigInteger, Boolean, Column, DateTime, String
from werkzeug.security import check_password_hash, generate_password_hash
from common.db import db


class UserModel(db.Model):
    """
    Model for user management
    +++++++++++++++++++++++++
    """

    __tablename__ = "users"

    id = Column("user_id", BigInteger, primary_key=True, autoincrement=True)
    username = Column(String(100), nullable=False, index=True, unique=True)
    first_name = Column(String(32), nullable=False)
    last_name = Column(String(32), nullable=False)
    email = Column(String(100), unique=True, index=True)
    password_hash = Column(String(100))
    phone_number = Column(String(10), nullable=True)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    products = db.relationship('ProductModel', backref='user', lazy=True)
    created_at = Column(
        DateTime(timezone=True), default=db.func.now(), onupdate=db.func.now()
    )
    updated_at = Column(
        DateTime(timezone=True), default=db.func.now(), onupdate=db.func.now()
    )

    def __init__(
        self,
        username,
        first_name,
        last_name,
        email,
        password,
        phone_number,
        is_active,
        is_admin,
    ):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password_hash = self.set_password(password)
        self.phone_number = phone_number
        self.is_active = is_active
        self.is_admin = is_admin

    def json(self):
        return {
            'username': self.username,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'phone_number': self.phone_number
        }


    def set_password(self, password):
        return generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        """Represent instance as a unique string."""
        return "<User({username!r})>".format(username=self.username)
