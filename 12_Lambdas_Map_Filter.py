#normal function 
def squared(x):
    return x**2

#print(squared(5))

# lambda expression
y = lambda a: a**2  # lambda takes a, squares it and return to y
#print(y(6))

# mutliple parameters
x = lambda a,b: a+b
#print(x(10,20))

#map function
x=[1,2,3]
y=[4,5,6]

def product(a,b):
    return a*b

c = list(map(product, x, y)) # creating a list as a output of the map. 
# Passing x, y lists one by one as input to the product function and storing the result as list in c
#print(c)

#map with lambda
list1 = [1,2,3,4,5]

a = list(map(lambda x: x+x, list1)) # self summation of each value in the list
# Passing list1 one by one to lambda expression
#print(a)


# filter()
# lambda to check if a number is even or not
x = lambda a: (a%2==0) # this lambda expression have a condition to check
#print(x(48))

# Now we pass a list to this lambda using filter() function
list2 = [2,3,6,8,9,11,14,21,22]
even_list = list(filter(x, list2)) # we pass list2 to x which contains lambda expression with the help of
# filter and store in even_list
print(even_list)





