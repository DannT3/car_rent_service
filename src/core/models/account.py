from sqlalchemy.orm import Mapped, mapped_column, relationship
from core.models.base import Base
from models.user import UserModel
from src.common.enum import UserStatus


class AccountModel(Base):
    __tablename__ = "account"

    acc_id: Mapped[int] = mapped_column(unique=True, primary_key=True) #account identificator

    user: Mapped["UserModel"] = relationship(back_populates="accounts")
    status: Mapped["UserStatus"] = relationship(back_populates="accounts")



