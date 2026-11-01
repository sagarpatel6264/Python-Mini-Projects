import mysql.connector

def connect_to_database():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="game_server_db"
        )
        print("Connected to MySQL Database successfully!")
        return conn
    except Exception as e:
        print(f"Database Connection Error: {e}")
        return None

# db_connection = connect_to_database()
