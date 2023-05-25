
class Employee1:

    raise_amount = 1.02

    def __init__(self, first, last, pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first + '.' + last + '@test.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)


emp3=Employee1('Simr', 'Raina', 100000)
emp4=Employee1('Test', 'User', 200000)

Employee1.set_raise_amt(1.05)
print(Employee1.raise_amount)
print(emp3.raise_amount)
print(emp4.raise_amount)

emp_str_1 = 'John-Doe-12000'

new_emp_1 = Employee1.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)
