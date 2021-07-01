from database.utils.user import get_user
import json
async def follow_event(db, performer, target):
    query = """INSERT INTO events (user_id, performer, target, type, description, image) VALUES ($1, $2, $3, $4, $5, $6)"""
    performer = await get_user(db, id=performer)
    target_user = await get_user(db, id=target)
    image = performer.avatar_url
    performer_html = f'<b><a href="/user/{performer.id}"{performer.username}</a></b>'
    target_html = f'<b><a href="/user/{target_user.id}"{target_user.username}</a></b>'
    description = f'{performer_html} started following {target_html}.'
    followers = json.loads(performer.followers)
    for follower_id in followers:
        print(await db.execute(query, follower_id, performer.id, str(target_user.id), "follow", description, image))
    description = f'{performer_html} started following you.'
    print(await db.execute(query, target_user.id, performer.id, str(target_user.id), "follow", description,image))