import sys

sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())
i=0

def greet():
    global i
    i+=1
    print('aniket',i)
    greet()
greet()          





