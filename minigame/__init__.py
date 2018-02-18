import sys
from minigame.Player import Type


def game():
    type_number = choose_player_type ()
    print("You have selected type ",type_number)
    sys.exit ("Game over. Come soon!")

def choose_player_type():
    player_types = Type.get_possible_types()
    type_selected = None
    try:
        type_number = int(input ("Choose type: "))
        if type_number>Type.__len__():
            print ("Ooops, invalid number. Try again")
            type_selected = choose_player_type ()
        elif type_number == 0:
            sys.exit ("Thanks for playing. Come soon!")
        else:
            item = int (type_number - 1)
            type_selected = Type.__getitem__ (player_types[item])
    except ValueError:
        print ("Ooops, invalid selection. Try again")
        type_selected = choose_player_type ()

    return type_selected

game()