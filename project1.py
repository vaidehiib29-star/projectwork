print("Welcome to the intaractive personal data collector !")

name = input("Please Enter Your Name: ")
age = int(input("Please Enter Your Age: "))
height = float(input("Please Enter Height in meters: "))
favourite_number = int(input("Please Enter Your favourite number: "))

birth_year = 2026-age

print("\n Thank you! Here is the information we collected:\n")

print("Name :",name,"(Type :",type(name),",Memory Address:",id(name),")")
print("Age :",age,"(Type :",type(age),",Memory Address:",id(age),")")
print("Height :",height,"(Type :",type(height),",Memory Address:",id(height),")")
print("Favourite Number :",favourite_number,"(Type :",type(favourite_number),",Memory Address:",id(favourite_number),")")

height_as_int=int(height)

print("\n Type converstion demostraction :")

print("Original height:",height,"(flot)")
print("Converted height:",height_as_int,"(int)")

print("Your birth year is approximately :",birth_year,"(based on your age of",age,")")

print("Thank you for using the personal data collector. goodbye!")