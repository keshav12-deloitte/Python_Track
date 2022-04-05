#n=5
space=4
spacemiddle=1
n=int(input("enter rows"))
for i in range(n):
    if(i==0):
        print(" "*(n)+ "*")
    elif(i<n-1):
        print(" "*space + "*" + " "*spacemiddle +"*")
        space=space-1
        spacemiddle=spacemiddle+2
    elif(i==n-1):
        print(" "+"*"*((n*2)-1))

