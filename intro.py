#samples

print("Hello World!")#string
print(2)#int
print(5+3)#math
print(True)#bool(True or False)

#variables and concantination
name = "Tim" #string
age = 23 #int
last_name = "Sailer"
found = False
#concatination 
print("My name is " + name + "and I am " + str(age) + " years old.")
print(f"My name is {name}  {last_name}")

#challenge
animal = "bear"
car = "camaro"
year = 1969

print(f"My favorite car is the {year} {car}.")

#casting (change var type)
print (20+ int("20"))#this is casting, we changed string to int
print(20 + age)
print(20 + 2.98)

#user input
user_name = input("Enter your name: ")
print(f"Hello, {user_name}")
#keep in mind input always returns strings
new_age = int(input("enter your age: "))
print(age + new_age)


#challenge 2
people = input("how many people in party? ")
slices = input("how many slices? ")
pizza = int(slices) / int (people)
print(f"each get {pizza} slices")