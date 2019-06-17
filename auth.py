class Auth():
	users = list()
	passes = list()
	names = list()

	def __init__(self):
		file = open("data.csv", "r")
		for x in file:
			stream = x.split(",")
			self.users.append(stream[0])
			self.passes.append(stream[1])
			self.names.append(stream[2])

	def checkInput(self):
		return 0