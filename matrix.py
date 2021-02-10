import csv

class Matrix:
	def __init__(self, name):
		self.value = []
		with open(name, newline='') as f:
			r = csv.reader(f, delimiter=',')
			for x in r:
				self.value.append([])
				for y in x:
					self.value[-1].append(int(y))
		self.width = len(self.value[0])
		self.height = len(self.value)
	def __getitem__(self, x):
		return self.value[x[0]][x[1]]