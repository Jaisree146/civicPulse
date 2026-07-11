import bcrypt


class PasswordManager:

    @staticmethod
    def hash_password(password: str) -> str:
        password_bytes = password.encode("utf-8")
        hashed_password = bcrypt.hashpw(
            password_bytes,
            bcrypt.gensalt()
        )

        return hashed_password.decode("utf-8")

    @staticmethod
    def verify_password(password: str, password_hash: str) -> bool:
        return bcrypt.checkpw(
            password.encode("utf-8"),
            password_hash.encode("utf-8")
        )