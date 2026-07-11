from models.role import Role
from config.db import db


class RoleRepository:
   
    @staticmethod
    def get_by_id(role_id: int) -> Role | None:
        
        return db.session.get(Role, role_id)

    @staticmethod
    def get_by_name(role_name: str) -> Role | None:
        """Retrieve a role by its name."""
        return Role.query.filter_by(role_name=role_name).first()