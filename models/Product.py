from sqlalchemy import (
    BigInteger,
    Column,
    DateTime,
    Float,
    String,
    Text,
)

from common.db import db


class ProductModel(db.Model):
    """
    Model for product management
    +++++++++++++++++++++++++
    """

    __tablename__ = "products"

    id = Column("product_id", BigInteger, primary_key=True, autoincrement=True)
    asin = Column(String(10), nullable=False)
    name = Column(Text, nullable=False)
    price = Column(String(50), nullable=True)
    rating = Column(Float, nullable=True)
    description = Column(Text, nullable=True)
    user_id = Column(
        BigInteger, db.ForeignKey("users.user_id", ondelete="CASCADE"), nullable=False
    )
    comments = db.relationship("CommentModel", backref="product", lazy=True)
    created_at = Column(
        DateTime(timezone=True), default=db.func.now(), onupdate=db.func.now()
    )
    updated_at = Column(
        DateTime(timezone=True), default=db.func.now(), onupdate=db.func.now()
    )

    def __init__(self, asin, name, price, rating, description, user_id):
        self.asin = asin
        self.name = name
        self.price = price
        self.rating = rating
        self.description = description
        self.user_id = user_id

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<Product({id})".format(id=self.id)
