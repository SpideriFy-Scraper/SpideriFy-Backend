from sqlalchemy import (
    BigInteger,
    Boolean,
    Column,
    Date,
    DateTime,
    Float,
    String,
    Text,
)

from common.db import db


class CommentModel(db.Model):
    """
    Model for product management
    +++++++++++++++++++++++++
    """

    __tablename__ = "comments"

    id = Column("comment_id", BigInteger, primary_key=True, autoincrement=True)
    author = Column(String(100), nullable=False)
    title = Column(Text, nullable=False)
    content = Column(Text, nullable=False)
    is_verified = Column(Boolean, nullable=False, default=True)
    variant = Column(Text, nullable=True)
    rating = Column(Float, nullable=True)
    date = Column(String(256), nullable=False)
    sentiment = Column(String(32), nullable=True)
    summarized_content = Column(Text, nullable=True)
    product_id = Column(BigInteger, db.ForeignKey(
        "products.product_id", ondelete="CASCADE"), nullable=True)
    created_at = Column(
        DateTime(timezone=True), default=db.func.now(), onupdate=db.func.now()
    )
    updated_at = Column(
        DateTime(timezone=True), default=db.func.now(), onupdate=db.func.now()
    )

    def __init__(
        self, author, title, content, is_verified, variant, rating, date
    ):
        self.author = author
        self.title = title
        self.content = content
        self.is_verified = is_verified
        self.variant = variant
        self.rating = rating
        self.date = date

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<Comment({id})".format(id=self.id)
