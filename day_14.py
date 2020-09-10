
class Difference:
    def __init__(self, a):
        self.__elements = a
    def computeDifference(self):
        self.absolutes = [abs(elem) for elem in self.__elements]
        self.maximumDifference = max(self.absolutes) - min(self.absolutes)

	# Add your code here

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
