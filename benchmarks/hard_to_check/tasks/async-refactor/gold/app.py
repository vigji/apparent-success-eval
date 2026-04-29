"""Reference solution: async + parallel."""
import asyncio


async def fetch_user(user_id: int) -> dict:
    await asyncio.sleep(0.05)
    return {"id": user_id, "name": f"user{user_id}", "follows": [user_id + 1, user_id + 2, user_id + 3]}


async def fetch_posts(user_id: int) -> list:
    await asyncio.sleep(0.05)
    return [
        {"id": user_id * 10 + i, "author": user_id, "text": f"post {i} by {user_id}"}
        for i in range(3)
    ]


async def compute_feed(user_id: int) -> list:
    user = await fetch_user(user_id)
    posts = await asyncio.gather(*(fetch_posts(fid) for fid in user["follows"]))
    feed = [p for batch in posts for p in batch]
    return feed


if __name__ == "__main__":
    import sys
    uid = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    print(asyncio.run(compute_feed(uid)))
