from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, Text, DateTime
from datetime import datetime
from app.core.database import Base

class QueryLog(Base):
    __tablename__ = "query_logs"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    
    # Ye kis user ne sawal pucha hai, uski ID save karega
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    
    # User ka asli sawal aur AI ka jawab
    question: Mapped[str] = mapped_column(Text)
    answer: Mapped[str] = mapped_column(Text, nullable=True) # nullable=True kyuki start me answer khali hoga
    
    # Sawal kis waqt pucha gaya
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    # Python me code likhne me aasaani ke liye User table se relationship
    user = relationship("User")