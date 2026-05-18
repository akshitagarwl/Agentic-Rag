from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, Text
# Apna wahi base sancha import kar rahe hain
from app.core.database import Base

class Document(Base):
    __tablename__ = "documents"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    filename: Mapped[str] = mapped_column(String(255))
    
    # RELATIONSHIP: Ek Document ke bohot saare Chunks (tukde) hote hain
    # cascade="all, delete" ka matlab hai agar Document delete ho, toh uske saare chunks bhi delete ho jayein
    chunks: Mapped[list["Chunk"]] = relationship(back_populates="document", cascade="all, delete")

class Chunk(Base):
    __tablename__ = "chunks"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    
    # FOREIGN KEY: Ye column batayega ki ye tukda (chunk) kis Document se aaya hai
    document_id: Mapped[int] = mapped_column(ForeignKey("documents.id"))
    
    text: Mapped[str] = mapped_column(Text) # Chunk ka actual text

    # Wapas Document se jodna
    document: Mapped["Document"] = relationship(back_populates="chunks")