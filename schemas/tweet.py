def tweetEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "content": item["content"],
        "created_at": item["created_at"],
        "updated_at": item["updated_at"],
        "by": item["by"]
    }

def tweetsEntity(entity) -> list:
    return [tweetEntity(item) for item in entity]