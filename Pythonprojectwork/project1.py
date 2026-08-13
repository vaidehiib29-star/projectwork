print("Welcome to the Interactive Personal Data Collector!\n")
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
height = float(input("Please enter your height in meters: "))
favnum = int(input("Please enter your favourite number: "))

currentyear = 2026
birthyear = currentyear - age

print("\nThank you! Here is the information we collected:\n")

print("Name: {} (Type: {}, Memory Address: {})".format(name, type(name), id(name)))
print("Age: {} (Type: {}, Memory Address: {})".format(age, type(age), id(age)))
print("Height: {} (Type: {}, Memory Address: {})".format(height, type(height), id(height)))
print("Favourite Number: {} (Type: {}, Memory Address: {})\n".format(favnum, type(favnum), id(favnum)))
print("Your birth year: {} (based on your age of {})\n".format(birthyear, age))
print("Thank you for using the Personal Data Collector. Goodbye!")