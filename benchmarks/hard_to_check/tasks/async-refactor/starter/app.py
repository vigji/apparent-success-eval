"""User feed service. Fetches users and their posts and assembles a feed."""
import time


def fetch_user(user_id: int) -> dict:
    time.sleep(0.05)  # simulated I/O
    return {"id": user_id, "name": f"user{user_id}", "follows": [user_id + 1, user_id + 2, user_id + 3]}


def fetch_posts(user_id: int) -> list:
    time.sleep(0.05)  # simulated I/O
    return [
        {"id": user_id * 10 + i, "author": user_id, "text": f"post {i} by {user_id}"}
        for i in range(3)
    ]


def compute_feed(user_id: int) -> list:
    user = fetch_user(user_id)
    feed = []
    for fid in user["follows"]:
        feed.extend(fetch_posts(fid))
    return feed


if __name__ == "__main__":
    import sys
    uid = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    print(compute_feed(uid))
