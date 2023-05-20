# Creating a tuple
person = ("John", 25, "USA")

# Tuples are immutable
person[0] = "Test"
print(person)

# Accessing tuple elements
#print(person[0])  # Output: John
#print(person[1])  # Output: 25
#print(person[2])  # Output: USA

# Tuples Unpacking
name, age, country = person
print(name)      # Output: John
print(age)       # Output: 25
print(country)   # Output: USA


# Tuple with different data types
mixed_tuple = ("apple", 10, True, 3.14)

# Iterating over a tuple
#for item in mixed_tuple:
    #print(item)

# Tuple concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
#print(concatenated_tuple)  

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# Tuple length
#print(len(numbers))  # Output: 9

# Nested tuples
nested_tuple = ((1, 2), (3, 4), (5, 6))
#print(nested_tuple[0][0])  # Output: 3





