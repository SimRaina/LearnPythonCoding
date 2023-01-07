nums = [2, 3, 5, 7]
for num in nums:
    print(num)


nums1 = [1,2,3,4]
for num in nums1:
    if(num==2):
        print(num)
        break
    print(num)

nums2 = [1,2,3,4]
for num in nums2:
    if(num==2):
        print("Found") # skips printing 2
        continue
    print(num)

# Nested For
num3 = [1, 2, 3]
for num in num3:
    for value in 'abc':
        print(num, value)


for i in range(10):
    print(i)

for i in range(1, 5):
    print(i)
