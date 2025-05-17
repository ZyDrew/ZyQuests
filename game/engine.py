from database.queries import *
from config.settings import PARTY
from classes.elf import Elf

def game_start(cur, conn):
    #Menu de départ
    #1. Nouvelle partie
    #2. Charger une partie
    #3. Quitter l'application
    print_start_screen()
    
    stay = True
    while(stay):
        ipt_menu = select_option_menu()

        match ipt_menu:
            case "1":
                ipt_user = input("Enter your username : ")
                if get_player_infos(ipt_user, cur) is None:
                    create_new_game(ipt_user, cur, conn)
                    stay = False
                    selected_class = player_select_class(ipt_user)
                    
                    match selected_class:
                        case "Dragon":
                            create_player(ipt_user, "Dragon", 1, 100, 40, 5, cur, conn)
                            #new_game_dragon()
                        case "Elf":
                            create_player(ipt_user, "Elf", 1, 100, 20, 5, cur, conn)
                            new_game_elf(ipt_user)
                        case "Giant":
                            create_player(ipt_user, "Giant", 1, 100, 20, 8, cur, conn)
                            #new_game_giant()
                else:
                    print("A party already exists with this name !\nLoad a game or choose another name")
            
            case "2":
                #Charger les parties existantes
                games = get_all_games(cur)
                if games:
                    for game in games:
                        print(f"{game[0]}. {game[1]} - last save : {game[2]}")
                    ipt_save = select_saved_game(games)
                    PARTY = load_game(ipt_save, cur)
                    stay = False
                else:
                    print("No party available\nCreate a new game with option 1")
            
            case "3":
                stay = False
    #End while stay

#Nouvelle partie pour la classe Elf
def new_game_elf(username):
    print("Game starting...")
    player = Elf(username, 1, 100, 20, 5, [], 10)
    print(player)

#Boucle principale du jeu
def main_game_process(cur, conn):
    game_running = True
    while(game_running):
        action = player_select_action_base()
        if action == "Exit":
            game_running = False
        print(action)
    #End while Game_Running

def select_option_menu():
    ipt_menu = input("Enter option : ")
    if ipt_menu in ("1", "2", "3"):
        return ipt_menu
    return select_option_menu()

def select_saved_game(games):
    ipt_save = input("Select your save : ")
    try:
        if int(ipt_save) >= 1 and int(ipt_save) <= len(games):
            return ipt_save
    except Exception:
        pass    
    return select_saved_game(games)

#Le joueur choisit une action
def player_select_action_base():
    print(r"""
[1] Move forward
[2] Search treasures
[3] Save game
[4] Exit
          """)
    stay = True
    while(stay):
        ipt_select = input("Enter your choice : ")
        if ipt_select in ("1", "2", "3", "4"):
            stay = False
    
    match ipt_select:
        case "1":
            return "Move forward"
        case "2":
            return "Search treasures"
        case "3":
            return "Save game"
        case "4":
            return "Exit"

#Le joueur selectionne une classe au départ de sa partie
def player_select_class(ipt_user):
        print(r"""
╔═══════════════════════════════════════════════════╗
║ Select your class                                 ║      
║                                                   ║       
║     Dragon : You gain extra mana & intelligence   ║
║     Elf    : You gain perception (traps disable)  ║
║     Giant  : You gain extra power                 ║
╚═══════════════════════════════════════════════════╝
[1] Dragon
[2] Elf
[3] Giant
    """)
        stay = True
        while(stay):
            ipt_class = input("Enter your choice : ")
            if ipt_class in ("1", "2", "3"):
                stay = False

        match ipt_class:
            case "1":
                return "Dragon"
            case "2":
                return "Elf"
            case "3":
                return "Giant"


#Ecran du menu principale au lancement du jeu
def print_start_screen():
    print(r"""
╔══════════════════════════════════════════════════╗
║                                                  ║
║           🛡️  WELCOME TO ZYQUESTS  ⚔️              ║
║                                                  ║
║     A fantasy text adventure where your fate     ║
║               lies in your choices.              ║
║                                                  ║
╚══════════════════════════════════════════════════╝
[1] New game
[2] Load game
[3] Exit
    """)
