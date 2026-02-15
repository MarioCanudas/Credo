from schemas import UserInfo, UserInfoProcessed


def process_user_info(user_info: UserInfo) -> UserInfoProcessed:
    return UserInfoProcessed()
