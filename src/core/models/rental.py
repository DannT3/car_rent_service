from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from core.models.base import Base
from core.models.user import UserModel
import datetime


class RentalModel(Base):
    __tablename__ = "rental"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(unique=True, ForeignKey="users.id")
    rented_at: Mapped[datetime.datetime] = mapped_column()
    user: Mapped[UserModel] = mapped_column(ForeignKey="users.name")