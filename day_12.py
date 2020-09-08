import functools as fn
class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores
        
    def calculate(self):
        self.score = fn.reduce(lambda a,b: a+b, self.scores)
        self.avg = self.score/len(self.scores)
        
        if self.avg in list(range(90,101)):
            return 'O'
        elif self.avg in list(range(80,90)):
            return 'E'
        elif self.avg in list(range(70,80)):
            return 'A'
        elif self.avg in list(range(55,70)):
            return 'P'
        elif self.avg in list(range(40, 55)):
            return 'D'
        elif self.avg < 40:
            return 'T'

line = input("Enter f,l,i: ").split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
scores = list( map(int, input("scores: ").split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade: ", s.calculate())
