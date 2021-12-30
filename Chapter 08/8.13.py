def build_profile(first, last, **user_info):
    """Строит словарь с информацией о пользователе."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile(
    'albert',
    'einstein',
    hobby='gym',
    nickname='F0rce',
    favorite_game='Dota 2',
)

full_name = user_profile['first_name'] + ' ' + user_profile['last_name']
print(f"{full_name.title()}'s information:\n{user_profile}.")
