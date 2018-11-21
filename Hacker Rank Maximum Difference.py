class Difference:
    elements=[]
    maximumDifference=0
    absdiff=0
    def __init__(self, a):
        self.elements = a
    def computeDifference(self):
        for i in self.elements:
            for j in range(len(self.elements)):
                self.absdiff=i-self.elements[j]
                if(self.absdiff>self.maximumDifference):
                    self.maximumDifference=self.absdiff
n=int(input())
l=[int(i) for i in input().split()]
o=Difference(l)
o.computeDifference()
print(o.maximumDifference)
