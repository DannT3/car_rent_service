from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.base import Base
from common.enum.car_type import CarType


class CarModel(Base):
    __tablename__ = "car"

    car_id: Mapped[int] = mapped_column(unique=True, index=True, primary_key=True)
    brand: Mapped[str] = mapped_column()
    model: Mapped[str] = mapped_column()
    year: Mapped[int] = mapped_column()
    car_type: Mapped["CarType"] = mapped_column()

