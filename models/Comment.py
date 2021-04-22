from app import db
from sqlalchemy import String, Integer, Boolean, Column, DateTime, Date, BigInteger,Text, ForeignKey ,Float
from datetime import datetime



class CommentModel(db.Model):
    """
     Model for product management
     +++++++++++++++++++++++++
    """
    __tablename__ = 'commnets'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    author = Column(String(100), nullable=True)
    title = Column(Text, nullable=False)
    content = Column(Text, nullable=False)
    is_verified = Column(Boolean, nullable=False, default=True)
    variant = Column(Text, nullable=False)
    rating = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
    product_id = Column(BigInteger, db.ForeignKey('ProductModel.id'))
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

