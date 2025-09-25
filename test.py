import random
def count():
    x=10
    while x>=0:
        print(x)
        x=x-1
def color():
    x="no"
    while not x==0:
        x=input("What is your favorite color?")
        if x=="Stop" or x=="stop":
            x=0
def game():
    x=0
    y=random.randint(1,10)
    i=0
    list=[]
    while not x==y:
        x=int(input("Choose your number "))
        if x>y:
            print("Less Than")
            list.append(x)
            print(list)
        elif x<y:
            print("Greater Than")
            list.append(x)
            print(list)
        else:
            print("Win")
            for i in range(i):
                print(list[i])
                i=i+1
game()