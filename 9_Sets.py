fruits = {"apple", "banana", "orange"}
#print(fruits)

fruits = {"apple", "banana", "orange", "apple"}
#print(fruits)

numbers = set([1, 2, 3, 4, 5])
#print(numbers)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union
union_set = set1.union(set2)
#print(union_set)
# Output: {1, 2, 3, 4, 5, 6, 7, 8}

# Intersection
intersection_set = set1.intersection(set2)
#print(intersection_set)
# Output: {4, 5}

# Difference
difference_set1 = set1.difference(set2)
#print(difference_set1)
# Output: {1, 2, 3}

# Difference
difference_set2 = set2.difference(set1)
#print(difference_set2)

# Check if a set is a subset of another set
subset_check = {1, 2}.issubset(set1)
print(subset_check)
# Output: True
