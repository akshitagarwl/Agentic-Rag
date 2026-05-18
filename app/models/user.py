from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
# Hamne jo base (Sancha) database.py me banaya tha, use yaha la rahe hain
from app.core.database import Base

class User(Base):
    # 1. Register (Table) ka asli naam jo database me dikhega
    __tablename__ = "users"

    # 2. Columns ki list
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String(255))
    plan: Mapped[str] = mapped_column(String(50), default="free")