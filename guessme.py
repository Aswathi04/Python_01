# GuessMe
import random

print("Do you think you can guess me?")


def guess_me(x):
    rand1 = random.randint(1, x-1)
    num = x
    randg=0
    while randg != rand1:
        randg = int(input(f"Guess a number between 1 and {num}"))
        if randg < rand1:
            print("Oops!,Too low")
        elif randg < rand1:
            print("Oops!,Too high")
        else:
            print(f"Bravo!,I am indeed the number {randg}")
            break;


guess_me(20)
