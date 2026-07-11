from config.db import db

class Department(db.Model):
    __tablename__ = "departments"
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    department_name = db.Column(
        db.String(100),
        nullable=False,
        unique=True
    )
    description = db.Column(
        db.Text,
        nullable=True
    )
    users=db.relationship("User",back_populates="department",lazy=True)