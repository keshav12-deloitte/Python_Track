


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






obj=PairsPossible(input("Enter the String: "))
c=obj.stringLength()
print(c)
obj.stringToCharactera()
obj.pairs()
obj.printPairs()
