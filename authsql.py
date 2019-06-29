import sqlite3
from sqlite3 import Error

class Auth():
	users = list()
	passes = list()
	names = list()
	connector = 0

	def __init__(self):
		database = "users.db" 
		try:
			self.connector = sqlite3.connect(database)
		except Error as e:
			print(e)


	def checkInput(self, user, pas):
		query = self.searchByUser(user)
		if query:
			if pas == query[0][1]:
				return 1, query[0][2] # Username and Password Match
			else:
				return 2, 0 # Username found, but password incorrect
		else:
			return 0, 0  # Username not found

	def searchByUser(self, user):
		cur = self.connector.cursor()
		cur.execute("SELECT * FROM Users WHERE Username LIKE ?", (user,))
		result = cur.fetchall()
		if result:
			return result #Username not found
		else:
			return False

	def addUser(self, user, pas, name):
		cursor = self.connector.cursor()