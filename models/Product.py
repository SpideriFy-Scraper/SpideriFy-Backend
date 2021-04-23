from app import db
from sqlalchemy import String, Integer, Column, DateTime, BigInteger,Float, ForeignKey
from models import User


class ProductModel(db.Model):
    """
     Model for product management
     +++++++++++++++++++++++++
    """
    __tablename__ = 'products'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    asin = Column(String(10), nullable=False)
    name = Column(Text, nullable=False)
    price = Column(String(50), nullable=True)
    rating = Column(Float, nullable=True)
    description = Column(Text, nullable=False)
    user_id = Column(BigInteger, db.ForeignKey('users.id'))
    created_at = Column(DateTime(timezone=True), default=db.func.now(), onupdate=db.func.now())
    updated_at = Column(DateTime(timezone=True), default=db.func.now(), onupdate=db.func.now())

    def __init__(asin, name, price, rating, description, user_id):
        self.asin = asin
        self.name = name
        self.price = price
        self.rating = rating
        self.description = description
        self.user_id = user_id
