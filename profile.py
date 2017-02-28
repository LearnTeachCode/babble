
class Profile:
  def __init__(self, firstname,lastname, username, email, new_number):
	   self.firstname = firstname 
	   self.lastname = lastname
	   self.username = username
	   self.email = email
	   self.new_number = new_number

	# firstname -> getters and setters
  def firstname(self, firstname):
		self.firstname = firstname

  @property
  def firstname(self):
    print "getter of firstname called"
    return self.firstname

  @firstname.set 
  def firstname(self, value):
   	print "setter of firstname called"
   	self.firstname = value

  @firstname.deleter
  def firstname(self):
    print "deleter of firstname called"
    del self.firstname

  # getters and setters -> lastname
  def lastname(self, lastname):
		self.lastname = lastname

  @property
  def lastname(self):
    print "getter of lastname called"
    return self.lastname

  @lastname.set 
  def lastname(self, value):
    print "setter of lastname called"
    self.firstname = value

  @lastname.deleter
  def lastname(self):
   	print "deleter of lastname called"
    del self.lastname

   	# getters and setters -> phonenumber
  def new_number(self, new_number):
	  self.new_number = new_number

  @property
  def new_number(self):
    print "getter of phonenumber called"
    return self.new_number

  @new_number.set 
  def new_number(self, value):
   	print "setter of new_number called"
   	self.new_number = value

  @new_number.deleter
  def new_number(self):
    print "deleter of new_number called"
    del self.new_number



    #def print_info(self):
        #print self.username, "<" + self.email + ">" 
