import psycopg2

def create_connection():
    conn = psycopg2.connect(
        database = "zyquests_db",
        user = "zydrew",
        password = "admin",
        host = "localhost"
    )

    return conn

def create_new_cursor(conn):
    return conn.cursor()

def stop_db_connection(cur, conn):
    cur.close()
    conn.close()