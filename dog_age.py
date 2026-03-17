name = input("Hi! What is your dogs name? ")
own = input(f"Have you owned {name} longer than 12 months?")
if own == "yes":
    years = int(input("How many years have you owned {name}? "))
    age = years * 7
    print(f"{name} is {age} in dog years!")
else:
    months = int(input("How many months have you owned {name}? "))
    age_a = months/12
    age2 = age_a * 7
    print(f"{name} is {age2:.1f} in dog years")