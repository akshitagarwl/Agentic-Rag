import asyncio
import time

async def fetch_database():
    print("1. Vector Database se data dhoondh rahe hain...")
    await asyncio.sleep(2)  # Maan lijiye DB ko 2 second lagte hain
    print("   -> Database se chunks mil gaye!")
    return "DB Chunks"

async def fetch_llm():
    print("2. OpenAI API ko call kar rahe hain...")
    await asyncio.sleep(3)  # Maan lijiye LLM ko 3 second lagte hain
    print("   -> LLM ka answer mil gaya!")
    return "LLM Answer"

async def main():
    start_time = time.time()
    
    print("--- Parallel Tasks Shuru ---")
    # asyncio.gather dono function ko ek hi time par start kar deta hai
    results = await asyncio.gather(
        fetch_database(),
        fetch_llm()
    )
    
    end_time = time.time()
    print(f"\nTotal time laga: {end_time - start_time:.2f} seconds.")
    print(f"Final Results: {results}")

if __name__ == "__main__":
    asyncio.run(main())