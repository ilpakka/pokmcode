map = [0, 0, 0], [0, 1, 0], [0, 0, "p"]
player = "x"
# x = player   p = goal   0 = free space    1 = block

map[0][0] = player
player_last_location = True
# setting the default player spawn coordinates 0,0

def map_print():
    """ Prints the current map layout"""
    for i in range(len(map)):
        for j in range(len(map[i])):
            print(map[i][j], end=' ')
        print()
    return

def player_location_reset():
    """ Resets the previous location of player
        back to a free space '0'
    """
    if player_last_location == True or 0:
        for i in range(len(map)):
            for j in range(len(map[i])):
                if map[i][j] == "x":
                    map[i][j] = 0
    return

def player_movement(direction):
    """ Player movement directions are called with this function
        player_movement(up):
            player = map[0 + 1, 0]
    """
    player_location_reset()

    if direction == "up":
        map[0 - 1][0] = player
    elif direction == "down":
        map[0 + 1][0] = player
    elif direction == "left":
        map[0][0 + 1] = player
    elif direction == "right":
        map[0][0 - 1] = player
    else:
        print("Invalid command")
        map[0][0] = player
    return

def start():
    """ This starts the instance """

    while(True):
        map_print()

        if player_last_location == False:
            break

        print("Which way would you like to go:")
        print("Up, Down, Left or Right?")
        player_movement_choice = input("Your choice:")
        player_movement(player_movement_choice.lower())

        # this is a sample test to show a single-turn run

start()
