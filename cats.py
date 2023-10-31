

"""
Goal: Create a class about my fav animal include data members about the animal

Class Animal

arms float
legs float 

def __init__():


def printattri():

"""


class Animal():

	def __init__(self, arms, legs, eyes, tail, fluffy):
		self.arms = arms
		self.legs = legs
		self.eyes = eyes
		self.tail = tail
		self.fluffy = fluffy


	def showItems(self):
		attris = {'Arms': self.arms, 'Legs': self.legs, 'Eyes': self.eyes, 'Has Tail': self.tail, 'Is Fluffy': self.fluffy}
		print(attris)

cat = Animal(2.5, 2.5, 2, True, True)


cat.showItems()
