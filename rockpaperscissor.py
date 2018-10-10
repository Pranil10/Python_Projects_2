import random
import time

options=['rock','paper','scissor']
def Player1():
    ch=input('enter rock or paper or scissor')
    global choice1
    choice1=ch.lower()
    while choice1 in options:
        Player2()
        break

def Player2():
    global choice2
    if mode==0:
        computer=['rock','paper','scissor']
        choice2=computer[random.randint(0,2)]
        print(choice2)
    else:
        ch2=input('Rock or paper or Scissor')
        choice2=ch2.lower()
    while choice2 in options:
        compare()
        break
    
def compare():
    if choice1==choice2:
        time.sleep(2)
        print("Its a Tie")
        
    elif choice1=='rock' and choice2=='scissor':
        time.sleep(2)
        print("Congraats  you win")
        
        
    elif choice1=='paper' and choice2=='rock':
        time.sleep(2)
        print("Congraats you win")
        
    elif choice1=='scissor' and choice2=='paper':
        time.sleep(2)
        print("Congraats you win")
        
    else:
        time.sleep(2)
        print("Player 2 wins")
        

          
    
print('WELCOME TO  MY GAME')
print('***************************************************')
print('0==Player vs Computer mode\n')
print('1==Player1 vs Player2 mode\n')
chances=3
gameisDone = False
mode=int(input('What mode do you want to play???'))
while chances>0:
    if mode==0 or mode==1:
        Player1()
        
    chances=chances-1

