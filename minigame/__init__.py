import sys
from minigame.Player import Type, Ethnic


def game():
    """
    :rtype: None
    """
    type_number = choose_player_type()
    ethnic_number = choose_player_ethnic()
    print("You have selected type ", type_number)
    sys.exit("Game over. Come soon!")


def choose_player_type():
    player_types = Type.get_possible_types()
    type_selected = None
    try:
        type_number = int(input ("Choose type: "))
        if type_number>Type.__len__():
            print ("Ooops, invalid number. Try again")
            type_selected = choose_player_type ()
        elif type_number == 0:
            sys.exit("Thanks for playing. Come soon!")
        else:
            item = int (type_number - 1)
            type_selected = Type.__getitem__ (player_types[item])
    except ValueError:
        print("Ooops, invalid selection. Try again")
        type_selected = choose_player_type()

    return type_selected


def choose_player_ethnic():
    player_ethnics = Ethnic.get_possible_ethnics()
    ethnic_selected = None
    try:
        ethnic_number = int(input ("Choose ethnic: "))
        if ethnic_number>Ethnic.__len__():
            print("Ooops, invalid number. Try again")
            ethnic_selected = choose_player_ethnic ()
        elif ethnic_number == 0:
            sys.exit ("Thanks for playing. Come soon!")
        else:
            item = int (ethnic_number - 1)
            ethnic_selected = Ethnic.__getitem__ (player_ethnics[item])
    except ValueError:
        print("Ooops, invalid selection. Try again")
        ethnic_selected = choose_player_ethnic()

    return ethnic_selected


game()