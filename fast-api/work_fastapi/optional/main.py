from typing import Optional

def get_profile(
	email: str,
 username: Optional[str] = None,
 age: Optional[int] = None,
) -> dict:
    profile = {'email': email}
    if username:
        profile['username'] = username
    if age:
        profile['age'] = age
    return profile


# 呼び出し
user_profile = get_profile(email = "user@example.com")
print(user_profile)


complete_profile = get_profile(
	email="user@example.com",
 username="user",
 age=30
)

print(complete_profile)