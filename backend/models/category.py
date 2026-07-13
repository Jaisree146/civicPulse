from datetime import datetime

from config.db import db


class Category(db.Model):

    __tablename__ = "categories"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    category_name = db.Column(
        db.String(100),
        nullable=False,
        unique=True
    )

    description = db.Column(
        db.String(255),
        nullable=True
    )

    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow
    )

    updated_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )
    issues = db.relationship(
    "Issue",
    back_populates="category",
    lazy=True
    )