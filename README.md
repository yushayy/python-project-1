# python-project-1This Python program implements a simple Rock-Paper-Scissors game where you can play against the computer.
How to Play
 * Save the code as rock_paper_scissors.py.
 * Run the program from your terminal using python rock_paper_scissors.py.
 * Choose your move by entering "rock", "paper", or "scissors" when prompted.
 * The computer will randomly select its move.
 * The winner will be determined based on the classic Rock-Paper-Scissors rules.
Dependencies
This program does not require any external libraries.
Example Usage
Rock, Paper, Scissors? rock
You chose: rock
Computer chose: scissors
You win!

Further Enhancements
 * Add scorekeeping to track wins, losses, and ties.
 * Implement a loop to allow for multiple rounds of play.
 * Improve the user experience with more informative messages.








import random
ccount=0;
ucount=0;
l=["rock","scissors","paper"]
while True:
    uc = int(input('''
game start
1 yes 
2 no|exit
    '''))
    if uc==1:
       for a in range(1,6):
        userinput=int(input('''
1 rock
2 scissors
3 paper
         ''' ))
        if userinput==1:
           uchoice="rock"
        elif userinput==2:
           uchoice="scissor"
        elif userinput==3:
           uchoice="paper"
        Cchoice=random.choice(l)
        if Cchoice==uchoice:
           print ("computer value",Cchoice);
           print ("user value",uchoice);
           print("game draw");
           ucount=ucount+1;
           ccount=ccount+1;
        elif (uchoice=="rock" and Cchoice=="scissor")or(uchoice=="scissor"and Cchoice=="paper")or(uchoice=="paper"and Cchoice=="rock"):
            print ("computer value",Cchoice);
            print ("user value",uchoice);
            print("you win");
            ucount=ucount+1;
        else:
           print ("computer value",Cchoice);
           print ("user value",uchoice);
           print("computer win");
           ccount=ccount+1;
           
        if(ucount==ccount):
         print("final game draw")
         print("user score",ucount)
         print("coumputer score",ccount)
        elif(ucount>ccount):
         print("user wins")
         print("user score",ucount)
         print("coumputer score",ccount)
        else:
         print("computer wins")
         print("user score",ucount)
         print("coumputer score",ccount)
        
    else: 
       break
