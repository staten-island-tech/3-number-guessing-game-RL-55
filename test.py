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
    x=11
    while not x==random:
        print(random)
print(random.randint(1,10))