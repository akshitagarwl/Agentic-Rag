import json
from functools import wraps
from app.core.redis_client import redis_client

def cache_response(expire_seconds=60): 
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
           
            cache_key = f"{func.__name__}:{str(args)}:{str(kwargs)}"
            
            cached_data = await redis_client.get(cache_key)
            if cached_data:
                print("⚡ FAST ANSWER (Cache Hit): Manager ki table se turant mil gaya!")
                return json.loads(cached_data)
            
            print("🐢 SLOW WORK (Cache Miss): Asli Godown/AI se mangwa rahe hain...")
            result = await func(*args, **kwargs)
            
            await redis_client.set(cache_key, json.dumps(result), ex=expire_seconds)
            
            return result
        return wrapper
    return decorator