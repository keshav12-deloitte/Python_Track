# 6

this_list = [[1, 1, 3, 2], [9, 8, 8, 1], [0, 4, 5, 0, 0, 1, 4]]
# print(this_list)
for i in this_list:
    listdup = i
    #print(listdup)

    for i in range(len(listdup)):
        count = 1
        for j in range(i+1,len(listdup)):
            if (listdup[i] == listdup[j]):
                count = count + 1

        if (count >= 2):
            print("{} => {}".format(listdup[i],(count)))
