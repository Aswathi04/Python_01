print("Lets play a game: ");
name=input("Your name? ")
print("ROCK")
print("PAPER")
print("SCISSORS")
s_c=0
s_y=0
import random
def game():
    global s_c,s_y
    if(c==y):
        print("You both guessed the same!")
    elif((c=="rock" and y=="paper") or( c=="paper" and y=="scissors") or (c=="scissors" and y=="rock")):
        print(f"Your choice {y} beats computer's choice {c}")
        s_y+=1
    else:
        print(f"Computer's choice {c} beats your choice {y}")
        s_c+=1

#computer:c,you:y
i=0
while (i<5):
    l=["rock","paper","scissors"]
    c=random.choice(l)
    y=input("Enter your choice: ")
    y=y.lower()
    game()
    i+=1
    

def winner():
    if(s_y>s_c):
        print(f"{name} wins!")
    else:
        print(f"Lost!,Better luck next time {name} :)")
winner()








