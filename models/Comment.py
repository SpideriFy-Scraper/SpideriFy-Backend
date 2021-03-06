from common.db import db
from sqlalchemy import String, Integer, Boolean, Column, DateTime, Date, BigInteger,Text, ForeignKey ,Float
from datetime import datetime



class CommentModel(db.Model):
    """
     Model for product management
     +++++++++++++++++++++++++
    """
    __tablename__ = 'comments'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    author = Column(String(100), nullable=False)
    title = Column(Text, nullable=False)
    content = Column(Text, nullable=False)
    is_verified = Column(Boolean, nullable=False, default=True)
    variant = Column(Text, nullable=True)
    rating = Column(Float, nullable=True)
    date = Column(Date, nullable=False)
    sentiment = Column(String(32), nullable=True)
    product_id = Column(BigInteger, db.ForeignKey('products.id'))
    created_at = Column(DateTime(timezone=True), default=db.func.now(), onupdate=db.func.now())
    updated_at = Column(DateTime(timezone=True), default=db.func.now(), onupdate=db.func.now())

    def __init__(author, title, content, is_verified, variant, rating, date, product_id):
        self.author = author
        self.title = title
        self.content = content
        self.is_verified = is_verified
        self.variant = rating
        self.date = date
        self.product_id = product_id

