stu_dict = {'name': 'John', 'age': 25, 'courses': ['Math', 'Science']}

print(stu_dict)
print(stu_dict['name'])
print(stu_dict.get('phone'))
print(stu_dict.get('phone', 'Not Found'))

stu_dict['phone'] = '11 111 111'
print(stu_dict.get('phone', 'Not Found'))

stu_dict['phone'] = '22 111 111' # update the existing value of the existing key

print(stu_dict.get('phone', 'Not Found'))

stu_dict.update({'name': 'Doe', 'age': 28})
print(stu_dict)

# del stu_dict['age']
# print(stu_dict)
#
# name = stu_dict.pop('name')
# print(name)
# print(stu_dict)

print(len(stu_dict))
print(stu_dict.keys())
print(stu_dict.values())
print(stu_dict.items())

for key, value in stu_dict.items():
    print(key, value)
