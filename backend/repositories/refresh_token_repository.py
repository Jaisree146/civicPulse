from config.db import db
from models.refresh_token import RefreshToken


class RefreshTokenRepository:

    @staticmethod
    def create(refresh_token: RefreshToken) -> RefreshToken:
        db.session.add(refresh_token)
        db.session.commit()

        return refresh_token

    @staticmethod
    def get_by_token_hash(token_hash: str) -> RefreshToken | None:
        return RefreshToken.query.filter_by(
            token_hash=token_hash
        ).first()

    @staticmethod
    def get_active_token_by_user_id(user_id: int) -> RefreshToken | None:
        return RefreshToken.query.filter_by(
            user_id=user_id,
            is_revoked=False
        ).first()

    @staticmethod
    def revoke(refresh_token: RefreshToken) -> None:
        
        refresh_token.is_revoked = True
        db.session.commit()

    @staticmethod
    def delete(refresh_token: RefreshToken) -> None:
    
        db.session.delete(refresh_token)
        db.session.commit()