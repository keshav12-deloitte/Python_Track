lst1=["Netflix", "Hulu", "Sling", "Hbo"]

lst2=[198, 166, 237, 125]

"""
dict={}
for i in range(len(lst1)):
    dict.update({zip(lst1(i): lst2(i))})
"""
dict2=dict(zip(lst1,lst2))
print(dict2)