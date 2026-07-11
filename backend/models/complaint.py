from datetime import datetime

from config.db import db


class Complaint(db.Model):

    __tablename__ = "complaints"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    complaint_number = db.Column(
        db.String(20),
        nullable=False,
        unique=True
    )

    citizen_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    title = db.Column(
        db.String(255),
        nullable=False
    )

    description = db.Column(
        db.Text,
        nullable=False
    )

    latitude = db.Column(
        db.Float,
        nullable=False
    )

    longitude = db.Column(
        db.Float,
        nullable=False
    )

    status = db.Column(
        db.String(30),
        nullable=False,
        default="Submitted"
    )

    processed = db.Column(
        db.Boolean,
        nullable=False,
        default=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )

    citizen = db.relationship(
        "User",
        back_populates="complaints"
    )