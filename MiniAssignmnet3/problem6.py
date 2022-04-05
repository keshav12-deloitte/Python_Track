sampledict={
    "name": "Kelly",

    "age": 25,

    "salary": 8000,

    "city": "New york"
}
sampledict["location"] = sampledict.pop("city")
print(sampledict)