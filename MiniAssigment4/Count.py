lst1=["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]

no_of_a_A=list(map(lambda x :x.count("a")+x.count("A"),lst1))
print(no_of_a_A)