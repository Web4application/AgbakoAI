import aioredis
import json

redis = None

async def get_redis():
    global redis
    if redis is None:
        redis = await aioredis.from_url("redis://localhost")
    return redis

async def get_cached_treatment(symptom: str):
    r = await get_redis()
    cached = await r.get(symptom)
    if cached:
        return json.loads(cached)
    return None

async def set_cached_treatment(symptom: str, treatment: dict):
    r = await get_redis()
    await r.set(symptom, json.dumps(treatment), ex=3600)
