
"""
a=int(input("enter the value of a : "))
b=int(input("enter the value of b : "))
c=int(input("enter the value of c : "))
x=int(input("enter the value of x : "))

equation=[]
equation.append(a)
equation.append(b)
equation.append(c)
equation.append(x)
print(equation)
root=list(map(lambda a,b,c,x:a(x*x)+b(x)+c,))
print(root)
"""

output = lambda a, b, c, x: (a*x*x)+(b*x)+c
y = output(*map(int,input("enter numbers: ").split()))
print(y)

