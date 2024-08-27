import random


def myGame():
    userdead = False
    print("Welcome to the Game!")
    print("You have differnet places to explore.")
    print("move on and explore.")
    position = 0
    while position < 100:
        if userdead == True:
            rnd = random.randint(1, 5)
            position = random.randint(2, 8)
            userdead = False
            print(f"You have respawned at position {position}.")
            if rnd == 1:
                choice = 'left'
            elif rnd == 2:
                choice = 'right'
            elif rnd == 3:
                choice = 'up'
            else:
                choice = 'down'
        else:
            choice = input(
                f"position {position}: Choose your path (left/right/up/down,end): ")

        if choice.lower() == "left":
            if position > 4:
                print("you reached in the top and You found a treasure.\n.\n.\n.")
            else:
                print("You encountered a magical tree!!\n.\n.\n.")
        elif choice.lower() == "right":
            print("you are near the xyz tree\nYou found a hammer!\n.\n.\n.")
        elif choice.lower() == "up":
            if position >= 3:
                print("slow down you reached the abc river \n.\n.\n.\nwater ahead!!")
            else:
                print('you reached in the forest \n.\n.\n.')
        elif choice.lower() == "down":
            print("nothing here move on!")
        elif choice.lower() == "end":
            print("exiting game")
            return
        else:
            print(
                "Invalid choice. You must choose 'left' or 'right' or 'up' or 'down' .(end)")
            position = position - 1

        killPlayer = random.randint(1, 8)
        if killPlayer <= 3:
            userdead = True
            print(
                "Oh No a dragon is comming towards you \naa..a..a , ohhhhh \nyou died !!!\nrespaning in a random place ")

        position += 1


myGame()
