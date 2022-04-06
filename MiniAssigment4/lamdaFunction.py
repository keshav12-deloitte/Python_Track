
#using only lamda
a=int(input("enter the value of a : "))
b=int(input("enter the value of b : "))
c=int(input("enter the value of c : "))
x=int(input("enter the value of x : "))


output =lambda a, b, c, x: a * x * x + b * x + c
print(output(a,b,c,x))


#using lamda and map
output1=lambda a,b,c,x :a * x * x + b * x + c
y=output1(*map(int,input("enter the value").split()))
print(y)

