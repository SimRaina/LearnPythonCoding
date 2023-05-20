my_list = [1, "apple", 3.14, True]

#print(my_list[0])    # Output: 1
#print(my_list[1])    # Output: "apple"
#print(my_list[-1])   # Output: True
my_list[2] = 2.718   # Modifying the third element
#print(my_list)       # Output: [1, "apple", 2.718, True]

my_list.append("banana")    # Adds "banana" to the end
my_list.insert(1, "orange")  # Inserts "orange" at index 1
my_list.remove(2.718)        # Removes 2.718 from the list
popped_element = my_list.pop(0)   # Removes and returns the element at index 0
#print(len(my_list)) # Find length of the list


new_list = ['A', 2, 'C']
my_list.append(new_list)
#print(my_list)

#Reading this new list at index 4
#print(my_list[4])

#Reading 3nd element in the nested list
print(my_list[4][2])


