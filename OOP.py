#python OOP programming
class employee:
	raise_amount = 1.04 #CLASS VARIABLE; data that is shared among all instances unlike instance variables.
	no_of_emp = 0 #class variable
	def __init__(self, first, last, pay): #PYTHON CONSTRUCTOR
	 #self represents an instance of a class. It is declared explicitly in python when a method of a class is defined.
	 #attributes/ instance variables
		self.first = first 
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'
		employee.no_of_emp += 1 #increases number of employees by 1 every time an instance is created.

	 #method to get the full name
	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	 #method for pay raise
	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount) 
		'''OR int(self.pay * employee.raise_amount) ; a class variable is either accessed through the class or its instance(self);
		 self should be used when the value of the variable needs to be different for some instance   '''

	 #CLASS METHOD to update raise_amount ; a class method is a method which takes a class as the first argument instead of an instance(self)
	@classmethod 
	def set_raise_amt(cls, amount):
		cls.raise_amount = amount

	@classmethod
	def from_string(cls, emp_str):
		first, last, pay = emp_str.split('-')
		return cls(first, last, pay)
   	 
   	 #STATIC METHOD is a method which does not access the instance or the class anywhere within the function but is logically connected to them
   	@staticmethod
   	def is_workday(day): #static method does not take the instance or the class as first argument
   		pass




emp1 = employee("Kalmia","Roots",20000) #object/ instance emp1 is created and is passed implicitly as self to the init method 
emp2 = employee("Test","User",70000) #object/ instance emp2 is created and is passed implicitly as self to the init method

#calling methods on object
#calling a method without parenthesis would return the method itself and not its return value
emp1.fullname() #OR employee.fullname(emp1)
emp2.apply_raise() #raises pay for emp2

employee.raise_amount = 2.07 
'''updating the value of a class variable through the class ; this will update raise_amount for all its instances because for now 
all instances are actually pointing to a single copy of the variable.
this is equivalent to employee.set_raise_amt(2.07)'''

emp2.raise_amount = 3.14 #this will only update the variable value for emp2 by creating a separate copy of this varaiable for emp2
employee.raise_amount = 5  #this will now update raise_amount for all instances of the class except for the instance emp2

print(employee.no_of_emp) #print number of employees

#using CLASS METHOD AS ALTERNATIVE CONSTRUCTOR to create objects
#this can be used when parameters are not given in a straightforward way
emp3_str = 'John-Bear-45000' #parameters for emp3 given in a string
emp_3 = employee.from_string(emp3_str) #calling from_string class method to create object
