
class Profile:
	def __init__(self, firstname,lastname, username, phonenumber,email):
		self.firstname = firstname 
		self.lastname = lastname
		self.username = username
		self.phonenumber = phonenumber
		self.email = email

	# user should be able to change username, phone number 
	def user(self, user1):
		self.username = user1

	def phone(self, phone1):
		self.phonenumber = phone1

    #def print_info(self):
        #print self.username, "<" + self.email + ">" 

