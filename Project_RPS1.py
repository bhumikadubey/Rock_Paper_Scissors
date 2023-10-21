# Rock Paper Scissor
import random
def gameWin(comp, you):
    # If two values are equal, declare a tie!
    if comp == you:
        return None

    # Check for all posibilities when computer choose r
    elif comp == 'r':
        if you == 's':
            return False
        elif you == 'p':
            return True

    # Check for all posiblities when computer choose p
    elif comp == 'p':
        if you == 's':
            return True
        elif you == 'r':
            return False
    
    # Check for all posiblities when computer choose s
    elif comp == 's':
        if you == 'p':
            return False
        elif you == 'r':
            return True
while True:
    print("Comp Turn: Rock(r) Paper(p) or Scissor(s)?")
    randNo = random.randint(1, 3)
    if randNo == 1:
        comp = 'r'
    elif randNo == 2:
        comp = 'p'
    elif randNo == 3:
        comp = 's'

    you = input("Your Turn: Rock(r) Paper(p) or Scissor(s)? ")
    a = gameWin(comp, you)

    print(f"Computer choose {comp}")
    print(f"You choose {you}")

    if a == None:
        print("The game is a tie!")
    elif a:
        print("You Win!")
    else:
        print("You Lose!")
