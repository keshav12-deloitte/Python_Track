
space=4
spacemiddle=1

for i in range(5):
    if(i==0):
        print(" "*5 + "*"+ " "*4)
    elif(i<4):
        print(" "*space + "*" + " "*spacemiddle +"*" + " "*space)
        space=space-1
        spacemiddle=spacemiddle+2
    elif(i<=5):
        print(" "+ "*"*9)

