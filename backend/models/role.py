from config.db import db


class Role(db.Model):

    __tablename__ = "roles"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    role_name = db.Column(
        db.String(50),
        nullable=False,
        unique=True
    )

    users = db.relationship(
        "User",
        back_populates="role",
        lazy=True
    )