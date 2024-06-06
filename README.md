# python-project-1
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
