#GAME QUERIES
def create_new_game(username, cur, conn):
    cur.execute("INSERT INTO game (name, location, quest) VALUES (%s, 1, 1)", (username,))
    conn.commit()

def get_all_games(cur):
    cur.execute("SELECT id, name, last_save from game")
    return cur.fetchall()

def load_game(id, cur):
    cur.execute("SELECT * FROM game WHERE id=%s", (id,))
    return cur.fetchone()

#PLAYER QUERIES
def get_player_infos(username, cur):
    cur.execute("SELECT * FROM player WHERE username=%s", (username,))
    return cur.fetchone()

def create_player(username, player_class, level, health, mana, power, cur, conn):
    cur.execute("INSERT INTO player (username, class, level, health, mana, power) VALUES (%s, %s, %s, %s, %s, %s)",
                (username, player_class, level, health, mana, power,))
    conn.commit()