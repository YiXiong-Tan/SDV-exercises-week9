# the 'class' key word to specify if this is a class
class Employee:

  # all classes is advice to have the __init__ function.
  # for functions in the class, it is always important to pass in 'self' as param
  # 'self' points to the instance the class
  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.pay = pay
    self.email = first+"."+last+"@company.com"

  # must always pass in 'self' so that the function knows that 
  def fullname(self):
    return '{} {}'.format(self.first, self.last)

# initialize the Employee class and assign to emp_1
emp_1 = Employee("Ian", "Tan", 50000)

# --------------------------------------------------------------------------------------
# we can access the class variables in the Employee Class
# notice that we don't have to pass in the instance as python will do this on it's own
# ---------------------------------------------------------------------------------------
# access the email
print(emp_1.email)

# call a function in the class
print(emp_1.fullname())

# another way to access the function in the class
print(Employee.fullname(emp_1))

