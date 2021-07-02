from database.utils.user import get_user
import json

async def follow_event(db, performer, target):
    query = """INSERT INTO events (user_id, performer, target, type) VALUES ($1, $2, $3, $4) ON CONFLICT (user_id, performer, target, type) DO UPDATE SET timestamp = NOW()::TIMESTAMP WITHOUT TIME ZONE"""
    performer = await get_user(db, id=performer)
    target_user = await get_user(db, id=target)
    followers = json.loads(performer.followers)
    for follower_id in followers:
        await db.execute(query, follower_id, performer.id, str(target_user.id), "follow-user")
    await db.execute(query, target_user.id, performer.id, str(target_user.id), "follow-you")


async def review_event(db, performer, target):
    query = """INSERT INTO events (user_id, performer, target, type) VALUES ($1, $2, $3, $4)"""
    performer = await get_user(db, id=performer)
    followers = json.loads(performer.followers)
    for follower_id in followers:
        await db.execute(query, follower_id, performer.id, str(target), "post-review")