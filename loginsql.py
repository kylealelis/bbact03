import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.uic import loadUi
import authsql as busi

class Login(QMainWindow):
	def __init__(self):
		super(Login, self).__init__()
		loadUi('login.ui',self)
		self.setWindowTitle('Login')
		self.loginButton.clicked.connect(self.onLoginClicked)
		self.regButton.clicked.connect(self.onRegClicked)
		self.Auth = busi.Auth()
	@pyqtSlot()

	def checkEdits(self):
		if (self.userEdit.text() == "" and self.passEdit.text() == ""):
			self.displayLabel.setText("Please enter a username and a password.")
		elif (self.userEdit.text() == ""):
			self.displayLabel.setText("Please enter a username.")	
		elif (self.passEdit.text() == ""):
			self.displayLabel.setText("Please enter a password.")
		else:
			return True

	def onLoginClicked(self):
		if self.checkEdits():
			flag, name = self.Auth.checkInput(self.userEdit.text(), self.passEdit.text())
			if flag == 1:
				self.displayLabel.setText("Welcome " + name + "!")
			elif flag == 2:
				self.displayLabel.setText("Wrong password, please try again.")


	def onRegClicked(self):
		inputUser = self.userEdit.text()
		if self.nameEdit.text() == "":
			self.displayLabel.setText("To register, please enter your name.")
		elif self.checkEdits():
			if self.Auth.searchUser(inputUser):
				self.displayLabel.setText("Username already taken.")
			else:
				self.Auth.addUser(self.userEdit.text(), self.passEdit.text(), self.nameEdit.text())
				self.displayLabel.setText("User successfully added!")


app = QApplication(sys.argv)
widget = Login()
widget.show()
sys.exit(app.exec_())