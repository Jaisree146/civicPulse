from config.db import db
from models.role import Role


def seed_roles():

    roles = [
        "Citizen",
        "Municipal Officer",
        "Department Officer"
    ]

    for role_name in roles:

        exists = Role.query.filter_by(
            role_name=role_name
        ).first()

        if exists is None:
            db.session.add(
                Role(
                    role_name=role_name
                )
            )

    db.session.commit()

    print("Roles seeded successfully.")