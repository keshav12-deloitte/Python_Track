with open("data.txt") as f:
    # print(f.read().split())
    ls1 = f.read().split()

print(ls1)
for i in range(len(ls1)):
    count1=len(ls1[i])
    for j in range(1,len(ls1)-1):
        count2=len(ls1[j])


