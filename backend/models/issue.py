from datetime import datetime

from config.db import db

from common.constants import IssueStatus
class Issue(db.Model):

    __tablename__ = "issues"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    issue_number = db.Column(
        db.String(20),
        unique=True,
        nullable=False
    )

    category_id = db.Column(
        db.Integer,
        db.ForeignKey("categories.id"),
        nullable=False
    )

    department_id = db.Column(
        db.Integer,
        db.ForeignKey("departments.id"),
        nullable=True
    )

    summary = db.Column(
        db.Text,
        nullable=False
    )

    priority = db.Column(
        db.String(20),
        nullable=False
    )

    report_count = db.Column(
        db.Integer,
        nullable=False,
        default=1
    )

    status = db.Column(
    db.String(30),
    nullable=False,
    default=IssueStatus.PENDING_REVIEW
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

    category = db.relationship(
        "Category",
        back_populates="issues",
        lazy=True
    )

    department = db.relationship(
        "Department",
        lazy=True
    )

    complaints = db.relationship(
        "Complaint",
        back_populates="issue",
        lazy=True
    )
    