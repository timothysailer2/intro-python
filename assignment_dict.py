# 1. Creating a dictionary with key:value pairs
student = {
    "name": "John",
    "age": 20,
    "grade": "B"
}
print("Step 1 - Created dictionary:", student)
print("Length:", len(student))

# 2. Accessing values using keys
print("Step 2 - Access 'name':", student["name"])
print("Length:", len(student))

# 3. Adding a new key
student["major"] = "Computer Science"
print("Step 3 - After adding 'major':", student)
print("Length:", len(student))

# 4. Updating an existing value
student["grade"] = "A"
print("Step 4 - After updating 'grade':", student)
print("Length:", len(student))

# 5. Removing a key
student.pop("age")
print("Step 5 - After removing 'age':", student)
print("Length:", len(student))