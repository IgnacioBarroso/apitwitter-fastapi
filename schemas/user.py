def userEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "first_name": item["first_name"],
        "last_name": item["last_name"],
        "birth_date": item["birth_date"],
        "email": item["email"],
    }

def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]