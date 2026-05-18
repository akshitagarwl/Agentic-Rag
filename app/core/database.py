from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase

# 1. Database ka URL (Aapke docker-compose me set kiye gaye username:password ke hisaab se)
DATABASE_URL = "postgresql+asyncpg://admin:adminpassword@localhost:5432/agentic_rag"

# 2. Async Engine: Ye background me PostgreSQL se connection handle karega
engine = create_async_engine(DATABASE_URL, echo=True)

# 3. Session Maker: Har naye task ke liye ek naya connection banayega
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# 4. Base Class: Iske zariye hum aage chalkar apne saare Data Models (Tables) banayenge
class Base(DeclarativeBase):
    pass