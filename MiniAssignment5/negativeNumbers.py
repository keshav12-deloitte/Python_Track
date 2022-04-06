lst1=[-1000, 500, -600, 700, 5000, -90000, -17500]
def negative(x):
    if(x<0):
        return x+2*x
"""
filter(list(map(negative,lst1)),lst1)
"""
lst2=list(filter(negative,lst1))
print(lst2)
lst2=list(map(lambda x:x-2*x,lst2))
print(lst2)

#using map in filter
lst3=[-1000, 500, -600, 700, 5000, -90000, -17500]
lst4=list(map(lambda x:abs(x),(filter(lambda x:x<0,map(lambda x:x,lst3)))))
print(lst4)
