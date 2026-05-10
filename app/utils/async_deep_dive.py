import asyncio
import httpx
import time

# ---------------------------------------------------------
# TASK 1: Async Await (httpx format)
# ---------------------------------------------------------
async def fetch_data(client, url, name):
    print(f"[{name}] Sending request...")
    # httpx uses a simple 'await' for the request, no 'async with' needed here!
    response = await client.get(url)
    data = response.json()
    print(f"[{name}] Response received!")
    return {name: data.get("id") or data.get("name")}

# ---------------------------------------------------------
# TASK 2: Async Generators (async for)
# ---------------------------------------------------------
# LLMs stream their responses token-by-token. This is how they do it.
async def mock_llm_stream():
    words = ["This", "is", "a", "simulated", "LLM", "streaming", "response."]
    for word in words:
        await asyncio.sleep(0.3) # Simulating generation time
        yield word # 'yield' inside an async def makes it an Async Generator

async def consume_stream():
    print("\n--- LLM Stream Starting ---")
    # 'async for' is required to loop over an async generator
    async for chunk in mock_llm_stream():
        print(chunk, end=" ", flush=True)
    print("\n--- Stream Ended ---\n")

# ---------------------------------------------------------
# MAIN EXECUTION
# ---------------------------------------------------------
async def main():
    urls = [
        ("Pokemon API", "https://pokeapi.co/api/v2/pokemon/pikachu"),
        ("Todo API", "https://jsonplaceholder.typicode.com/todos/1"),
        ("User API", "https://jsonplaceholder.typicode.com/users/1")
    ]
    
    start_time = time.time()
    
    # 'async with' safely opens and closes the main connection pool
    async with httpx.AsyncClient() as client:
        print("--- Firing parallel API requests ---")
        
        # asyncio.create_task() schedules them to run immediately
        tasks = [asyncio.create_task(fetch_data(client, url, name)) for name, url in urls]
        
        # gather() waits for all scheduled tasks to finish
        api_results = await asyncio.gather(*tasks)
        
    end_time = time.time()
    print(f"Total Network Time: {end_time - start_time:.2f} seconds.")
    print(f"API Results: {api_results}")
    
    # Now let's test the streaming generator
    await consume_stream()

if __name__ == "__main__":
    asyncio.run(main())