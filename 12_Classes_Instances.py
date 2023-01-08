class Employee:
    def __init__(self, first, last, role):
        self.first = first
        self.last = last
        self.role = role
        self.email=first+'.'+last+'@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp1 = Employee('Sim', 'Raina', 'QA')

print(emp1.email)
print(emp1.fullname())

print(Employee.fullname(emp1))
