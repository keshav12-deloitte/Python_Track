list1=["hello","take"]
list2=["dear","sir"]


for i in range(0,len(list1)):
    list1[0]=list1[0]+list2[0]
    list1[1] = list1[1] + list2[1]

print(list1)