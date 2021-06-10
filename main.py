import random as rand

def set_up():
    prize_door = rand.randint(1, 3)
    door_pick = rand.randint(1, 3)
    remove_door_list = [1, 2, 3]
    option_list = [1, 2, 3]


    if prize_door in remove_door_list:
        remove_door_list.remove(prize_door)
    if door_pick in remove_door_list:
        remove_door_list.remove(door_pick)

    remove_door = rand.choice(remove_door_list)
    option_list.remove(remove_door)

    return door_pick, prize_door, option_list
    print(door_pick, prize_door)
    print(remove_door_list)
    print(remove_door)
    print(option_list)

def no_switch():
    door_pick, prize_door, option_list = set_up()
    if door_pick == prize_door:
        return True

def switch():
    door_pick, prize_door, option_list = set_up()
    option_list.remove(door_pick)
    new_pick = option_list[0]
    if new_pick == prize_door:
        return True


def main():

    no_switch_win = 0
    switch_win = 0

    for i in range(1000):
        if no_switch() == True:
            no_switch_win += 1
        if switch() == True:
            switch_win += 1
    print("No switch win:", no_switch_win, "Switch win:", switch_win)




if __name__ == '__main__':
    main()