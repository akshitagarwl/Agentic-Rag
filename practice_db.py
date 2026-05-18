import asyncio
import time
from sqlalchemy import text, select
from app.core.database import AsyncSessionLocal
from app.models.user import User

async def main():
    # 1. Ek random email banate hain taaki baar-baar run karne par error na aaye
    random_email = f"user_{int(time.time())}@example.com"

    # 2. Godown ka darwaza (session) kholte hain
    async with AsyncSessionLocal() as session:
        
        # --- NAYA USER SAVE KARNA ---
        print(f"\n[+] {random_email} ko database me save kar rahe hain...")
        new_user = User(email=random_email, hashed_password="secretpassword123", plan="pro")
        session.add(new_user)
        await session.commit() # Save pakka karne ke liye commit zaroori hai

        # ==============================================================
        # TAREEKA 1: ORM (Naya Python Style)
        # ==============================================================
        print("\n--- 1. ORM Query (Python Style) ---")
        orm_query = select(User).filter_by(email=random_email)
        result_orm = await session.execute(orm_query)
        # scalar_one_or_none() hamari table ki row ko ek object me badal deta hai
        user_from_orm = result_orm.scalar_one_or_none() 
        print(f"ORM Jawab -> Email: {user_from_orm.email}, Plan: {user_from_orm.plan}")

        # ==============================================================
        # TAREEKA 2: Raw SQL (Purana Database Style)
        # ==============================================================
        print("\n--- 2. Raw SQL (Purana Style) ---")
        # Isme humein lamba SQL code manually text me likhna padta hai
        sql_query = text(f"SELECT * FROM users WHERE email = '{random_email}'")
        result_sql = await session.execute(sql_query)
        # fetchone() bas ek dictionary/tuple deta hai
        user_from_sql = result_sql.fetchone() 
        print(f"SQL Jawab -> Email: {user_from_sql.email}, Plan: {user_from_sql.plan}")

if __name__ == "__main__":
    asyncio.run(main())