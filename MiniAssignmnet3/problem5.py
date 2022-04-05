def merging(dict1,dict2):
        return (dict1.update(dict2))


dict1={
    'ten':10,
    'twenty':20,
    'thirty':30
}
dict2={
    'fourty':40,
    'fifty':50,
    'sixty':60
}

merging(dict1,dict2)
print(dict1)
