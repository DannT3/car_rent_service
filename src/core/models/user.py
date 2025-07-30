from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey


class UserModel(Base):
    __tablename__ = "user"

    