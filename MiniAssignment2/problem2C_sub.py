spacefirst=1
spacemiddle=2
for i in range(5):
    if(i==0):
        print("*"*5)
    elif(i<4):
        print(" "*spacefirst+"*"+" "*spacemiddle+"*")
        spacefirst=spacefirst+1
        spacemiddle=spacemiddle-1
    elif(i<5):
        print(" "*4 + "*")