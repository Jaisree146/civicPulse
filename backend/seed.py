from app import app


from seeds.seed_department import seed_departments
from seeds.seed_category import seed_categories
from seeds.seed_role import seed_roles

with app.app_context():

    seed_roles()
    seed_departments()
    seed_categories()

    print("All master data seeded successfully.")