from sqlalchemy_utils import UUIDType
from sqlalchemy import UniqueConstraint

from bookshop.sqlalchemy import db
from bookshop.sqlalchemy.model.types import BigIntegerVariantType


class Review(db.Model):  # type: ignore
    id =        db.Column(BigIntegerVariantType, primary_key=True, autoincrement=True)  # noqa: E501
    review_id = db.Column(UUIDType, index=True, nullable=False)  # noqa: E501
    text =      db.Column(db.String, index=True, nullable=False)  # noqa: E501
    book_id =   db.Column(db.BigInteger, db.ForeignKey('book.id'), nullable=True)  # noqa: E501
    book =      db.relationship(
        'Book',
        lazy=False,
        uselist=False,
        foreign_keys=[book_id],
    )

    __table_args__ = (UniqueConstraint('review_id', ), )
