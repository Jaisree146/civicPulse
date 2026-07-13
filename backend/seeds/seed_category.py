from config.db import db
from models.category import Category


def seed_categories():

    categories = [
        {
            "category_name": "Road Damage",
            "description": "Potholes, damaged roads, uneven surfaces."
        },
        {
            "category_name": "Drainage",
            "description": "Drainage overflow, sewage blockage."
        },
        {
            "category_name": "Water Leakage",
            "description": "Pipeline leakage and water wastage."
        },
        {
            "category_name": "Street Light",
            "description": "Street lights not functioning."
        },
        {
            "category_name": "Garbage",
            "description": "Garbage collection and waste disposal."
        }
    ]

    for category in categories:

        exists = Category.query.filter_by(
            category_name=category["category_name"]
        ).first()

        if exists is None:
            db.session.add(
                Category(**category)
            )

    db.session.commit()

    print("Categories seeded successfully.")