from database.connection import *
from game.engine import game_start, main_game_process

def main():
    conn = create_connection()
    cur = create_new_cursor(conn)
    game_start(cur, conn)
    main_game_process(cur, conn)

    stop_db_connection(cur, conn)

main()
    