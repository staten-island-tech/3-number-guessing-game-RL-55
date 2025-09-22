def count():
    x=10
    while x>=0:
        print(x)
        x=x-1
def color():
    x="no"
    while not x=="Stop" or not x=="stop":
        x=input("What is your favorite color? ")
        print(x)
color()