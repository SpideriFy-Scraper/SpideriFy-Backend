from app import db
from sqlalchemy import String, Integer, Boolean, Column, DateTime, BigInteger, ForeignKey
from models import User


class ProductModel(db.Model):
    """
     Model for product management
     +++++++++++++++++++++++++
    """
    __tablename__ = 'products'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, db.ForeignKey('users.id'))
    created_at = Column(DateTime(timezone=True), default=db.func.now(), onupdate=db.func.now())
    updated_at = Column(DateTime(timezone=True), default=db.func.now(), onupdate=db.func.now())
