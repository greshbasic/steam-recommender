import psycopg2
from config import POSTGRES_CONFIG, NEBULA_ID, FAKE_ID
from recommend_tools import handle_recommendation
from database_tools import connect_to_db, check_if_user_exists
        
def main():
    connect_to_db()
    steam_id = NEBULA_ID
    user_exists, tags = check_if_user_exists(steam_id)
    handle_recommendation(steam_id, user_exists, tags)

if __name__ == "__main__":
    main()
