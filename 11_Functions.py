# DRY -> Do Not Repeat Yourself
def func():
    pass


print(func())

def func1():
    print("Hello 1")

func1()


def func2():
    return 'Hello 2'

print(func2().upper())

def func3(name):
    return 'Welcome {} !'.format(name)

print(func3('SimRaina'))


def func4(name, greeting='Hello'):
    return '{}, {} !'.format(greeting, name)

print(func4('SimRaina'))

def func5(name, greeting='Hello'):
    return '{}, {} !'.format(greeting, name)

print(func4('SimRaina', 'Welcome'))

def emp_info(*args, **kwargs):
    print(args)
    print(kwargs)

emp_info('QA', 'IT', name='Sim', age='32')

def emp_info1(*args, **kwargs):
    print(args)
    print(kwargs)

dept_info = ['QA', 'IT']
info = {'name': 'Sim', 'age': 32}

emp_info1(*dept_info, **info)
