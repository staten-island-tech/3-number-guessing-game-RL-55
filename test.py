import random
def count():
    x=10
    while x>=0:
        print(x)
        x=x-1
def color():
    x="no"
    while not x==0:
        x=input("What is your favorite color? ")
        if x=="Stop" or x=="stop":
            x=0
def game():
    a=int(input("Min "))
    b=int(input("Max "))
    x=0
    y=random.randint(a,b)
    z=0
    guess_history=["Guess List;:"]
    while not x==y:
        x=int(input("Choose your number "))
        z=z+1
        if x>y:
            print("Less Than")
            guess_history.append(x)
            print(guess_history)
        elif x<y:
            print("Greater Than")
            guess_history.append(x)
            print(guess_history)
        else:
            print("You Win")
            for i in range(z):
                print(guess_history[i])
game()
