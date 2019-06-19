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
		searchIndex = 0
		for x in self.users:
			if x == user:
				if pas == self.passes[searchIndex]: # Password verification
					return 1, self.names[searchIndex] # User found, also returns name of user
				else:
					return 2, 0
					continue
			else:
				searchIndex += 1
				continue

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