#1. Defining the function

def greet():
    print("Hello, world!")

# To call this function to execute
greet()

#2. Function with arguments
def greet(name):
    print(name)

#call
greet('Sim')

#3. Return value
def add_numbers(a, b):
    return a + b

#call
print(add_numbers(1,2))

#4. Default argument
def greet(name="world"):
    print("Hello, " + name)

#call
greet() #no argument passed

#5. Any number of argument 
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

print(add_numbers())

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(key + ": " + str(value))

#call
print_info(name='Sim', dept='QA')




