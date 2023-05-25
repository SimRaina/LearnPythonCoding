class Employee:
    dept = 'IT' # class variable
    def __init__(self, first, last, role):
        self.first = first
        self.last = last
        self.role = role
        self.email=first+'.'+last+'@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def deptname(self):
         return self.dept
         # return Employee.dept

emp1 = Employee('Sim', 'Raina', 'QA')

print(emp1.email)
print(emp1.fullname())

print(Employee.fullname(emp1))
# print(emp1.deptname())
# emp1.dept = 'HR'
Employee.dept = 'HR'
print(emp1.dept)
print(Employee.dept)

# print(emp1.__dict__)
# print(Employee.__dict__)
