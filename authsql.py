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

	def checkInput(self, user, pas):
		if self.searchUser(user):
			if pas == self.passes[self.users.index(user)]:
				return 1, self.names[self.users.index(user)] # Username and Password Match
			else:
				return 2, 0 # Username found, but password incorrect
		else:
			return 0, 0  # Username not found

	def searchUser(self, user):
		usercount = self.users.count(user)
		if usercount < 1:
			return False #Username not found
		else:
			return True

	def addUser(self, user, pas, name):
		self.users.append(user)
		self.passes.append(pas)
		self.names.append(name)
		file = open ("data.csv", "a")
		file.write(user + "," + pas + "," + name + "\n")