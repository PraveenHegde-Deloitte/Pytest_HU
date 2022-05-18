class StringClass:

    def __init__(self,demo):
        self.demo=demo

    def list(self):
        return (list(self.demo))

    def length(self):
        return len(self.demo)

class PairsPossible(StringClass):

    def pairspossible(self,test_list):
        result = [(n,j) for idx,n in enumerate(test_list)for j in test_list[idx+1:]]
        print(result)

class SearchCommonElements(StringClass):

    def commonelements(self,str1,str2):
        str3 = list(set(str1) & set(str2))
        print(str3)

class EqualSumPairs():

    def Equalpair(self,test_list):
        uniqueSums=[]
        result = [sum((int(n),int(j))) for idx,n in enumerate(test_list) for j in test_list[idx+1:]]
        print(result)
        n=len(result)
        sums = dict()

        for num in range(n):
            if result[num] in sums.keys():
                sums[result[num]] += 1
            else:
                sums[result[num]] = 1
        for num in sums:
            if sums[num] == 1:
                uniqueSums.append(num)
        print(uniqueSums)
        print(len(uniqueSums))



string1=input("Enter a string :")
object1=StringClass(string1)
print(object1.list())
print(object1.length())
list1=object1.list()

object2=PairsPossible(object1)
object2.pairspossible(list1)

string2=input("Enter string to compare :")
object3=SearchCommonElements(list1)
object3.commonelements(string1,string2)

print('sum of pairs')
object4=EqualSumPairs()
object4.Equalpair(list1)