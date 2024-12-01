import psycopg2
import requests
from config import POSTGRES_CONFIG
from recommend_tools import recommend_games, determine_tags_for_user

def connect_to_db():
    try:
        conn = psycopg2.connect(**POSTGRES_CONFIG)
        print("Connection successful!")
        conn.close()
    except Exception as e:
        print(f"Connection failed: {e}")
        
def check_if_user_exists(steam_id):
    try:
        connection = psycopg2.connect(**POSTGRES_CONFIG)
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM users WHERE steamid={steam_id}")
        result = cursor.fetchone()
        if result:
            print(f"User with ID {steam_id} found!")
            return (True, result[1])
        print(f"User with ID {steam_id} not found.")
        return (False, None)
    except Exception as e:
        print(f"Error: {e}")
        return (False, None)
    finally:
        cursor.close()
        connection.close()
        
def main():
    connect_to_db()
    steam_id = int(input("Enter a Steam ID: "))
    user_exists, tags = check_if_user_exists(steam_id)
    if user_exists:
        recommend_games(tags)
    else:
        determine_tags_for_user(steam_id)
    

if __name__ == "__main__":
    main()
