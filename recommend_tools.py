def recommend_games(tags):
    pass

def determine_tags_for_user(steam_id):
    games = get_games_from_user(steam_id)
    tags = get_tags_from_games(games)
    # do math to get weighted tags
    # insert tags into database
    recommend_games(tags)

def get_games_from_user(steam_id):
    pass

def get_tags_from_games(games):
    pass
