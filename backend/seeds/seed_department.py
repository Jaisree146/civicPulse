from config.db import db
from models.department import Department


def seed_departments():

    departments = [
        {
            "department_name": "Roads",
            "description": "Handles road maintenance and potholes."
        },
        {
            "department_name": "Drainage",
            "description": "Handles drainage and sewage issues."
        },
        {
            "department_name": "Water Supply",
            "description": "Handles water supply and pipeline issues."
        },
        {
            "department_name": "Street Light",
            "description": "Handles street lighting issues."
        },
        {
            "department_name": "Waste Management",
            "description": "Handles garbage collection and sanitation."
        }
    ]

    for department in departments:

        exists = Department.query.filter_by(
            department_name=department["department_name"]
        ).first()

        if exists is None:
            db.session.add(
                Department(**department)
            )

    db.session.commit()

    print("Departments seeded successfully.")