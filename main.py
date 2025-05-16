from database.connection import *
from game.engine import game_start

def main():
    conn = create_connection()
    cur = create_new_cursor(conn)
    game_start(cur, conn)

    stop_db_connection(cur, conn)

main()
    