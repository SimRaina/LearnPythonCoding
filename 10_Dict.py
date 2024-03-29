student = {
    "name": "John",
    "age": 20,
    "major": "Computer Science"
}
#print(student)
#print(student["name"])
# Output: John

#print(student["age"])
# Output: 20

student["age"] = 21  # Modify the value of an existing key
student["year"] = 3  # Add a new key-value pair
#print(student)

del student["major"]
#print(student)


#print("name" in student)
# Output: True

#print(student.keys())
# Output: dict_keys(['name', 'age', 'year'])

#print(student.values())
# Output: dict_values(['John', 21, 3])

#print(student.items())

#for key in student:
    #print(key, student[key])


# Adding and Accessing Lists inside the Dictionary
country = {
    "US": ["Dallas", "Colorado", "Los Angeles"],
    "UK": ["London", "Manchester", "Liverpool"],
    "Germany": ["Berlin", "Munich", "Frankfurt"]
}

print(country["UK"])
print(country["UK"][0])
print(country["US"][1])
print(country['Germany'][2])




















