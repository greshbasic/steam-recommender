def recommend_games_from_tags(tags):
    pass

def determine_tags_for_user(steam_id):
    games = get_games_from_user(steam_id)
    tags = get_tags_from_games(games)
    # do math to get weighted tags
    # insert tags into database
    recommend_games_from_tags(tags)

def get_games_from_user(steam_id):
    pass

def get_tags_from_games(games):
    pass

def handle_recommendation(steam_id, user_exists, tags):
    if user_exists:
        recommend_games_from_tags(tags)
    else:
        determine_tags_for_user(steam_id)
