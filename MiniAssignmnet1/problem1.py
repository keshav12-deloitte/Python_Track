


class StringClass:

    def __init__(self, stringValue):
        self.stringValue = stringValue
        self.strlength=0
    def stringLength(self):
        self.strlength = len(self.stringValue)
        return self.strlength

    def stringToCharactera(self):
        stringList=list(self.stringValue)
        print(stringList)


class PairsPossible(StringClass):
    def pairs(self):
        self.st_arr = set()
        for i in range(len(self.stringValue)):
            for j in range(i+1,len(self.stringValue)):
                self.st_arr.add((self.stringValue[i],self.stringValue[j]))
        return self.st_arr
    def printPairs(self):
        print(self.st_arr)
    def lenPairs(self):
        print(len(self.st_arr))


class EqualSumPairs(PairsPossible):
    def sum(self):
        for i,j in self.st_arr:
            dict1={i+j}
        print(dict1)








obj=PairsPossible(input("Enter the String: "))
c=obj.stringLength()
print(c)
obj.stringToCharactera()
obj.pairs()
obj.printPairs()
obj1=EqualSumPairs(PairsPossible)
obj1.lenPairs()


