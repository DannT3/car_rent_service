from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from core.models.base import Base

class UserModel(Base):
    __tablename__ = "user"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    surname: Mapped[str] = mapped_column(unique=True)
    email_address: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str] = mapped_column(index=True, unique=False)




    

    