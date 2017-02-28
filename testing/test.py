class Person:
	'This is testing with class objects in Python'
	personCount = 0
	
	def __init__(self,name):
		self.name = name
		Person.personCount += 1
	
	def displayPerson(self):
		print "I am", self.name
	
	def displayPersonCount(self):
		print "There are %d people" %Person.personCount


a = Person("Hannah")
b = Person("Thomas")
a.displayPerson()
a.displayPersonCount()
