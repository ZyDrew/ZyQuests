import psycopg2

def get_player_infos(username, cur):
    cur.execute("SELECT * FROM player WHERE username=%s", (username,))
    return cur.fetchone()

def create_new_player(username, cur, conn):
    cur.execute("INSERT INTO player (username) VALUES (%s)", (username,))
    conn.commit()

def get_all_games(cur):
    cur.execute("SELECT * from player")
    return cur.fetchall()

def load_party(id, cur):
    cur.execute("SELECT * FROM player WHERE id=%s", (id,))