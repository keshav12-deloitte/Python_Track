from functools import reduce
lst1=[1,2,3,4,5,6,7]

mul=reduce(lambda x,y:x*y,lst1)
print(mul)