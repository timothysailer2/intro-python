# 1. Creating a list
fruits = ["apple", "banana", "cherry"]
print("Step 1 - Created list:", fruits)

# 2. Accessing items by index
print("Step 2 - First item:", fruits[0])

# 3. Replacing values
fruits[1] = "orange"
print("Step 3 - After replacing index 1:", fruits)

# 4a. Removing item by value
fruits.remove("cherry")
print("Step 4a - After removing 'cherry':", fruits)

# 4b. Removing item by index
fruits.pop(0)
print("Step 4b - After removing index 0:", fruits)

# 5. Printing the list and its length
print("Step 5 - Final list:", fruits)
print("Step 5 - Length of list:", len(fruits))