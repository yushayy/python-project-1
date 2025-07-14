import random

ccount = 0
ucount = 0
l = ["rock", "scissors", "paper"]

while True:
    uc = int(input('''
Game Start:
1. Yes 
2. No | Exit
    '''))
    if uc == 1:
        for a in range(1, 6):
            userinput = int(input('''
1. Rock
2. Scissors
3. Paper
            '''))
            if userinput == 1:
                uchoice = "rock"
            elif userinput == 2:
                uchoice = "scissors"
            elif userinput == 3:
                uchoice = "paper"
            else:
                print("Invalid input!")
                continue

            Cchoice = random.choice(l)

            print("Computer:", Cchoice)
            print("User:", uchoice)

            if Cchoice == uchoice:
                print("It's a draw!")
                ucount += 1
                ccount += 1
            elif (uchoice == "rock" and Cchoice == "scissors") or \
                 (uchoice == "scissors" and Cchoice == "paper") or \
                 (uchoice == "paper" and Cchoice == "rock"):
                print("You win!")
                ucount += 1
            else:
                print("Computer wins!")
                ccount += 1

        print("\nFinal Scores:")
        print("User:", ucount)
        print("Computer:", ccount)

        if ucount == ccount:
            print("Final game is a draw!")
        elif ucount > ccount:
            print("You are the overall winner!")
        else:
            print("Computer is the overall winner!")
    else:
        break

