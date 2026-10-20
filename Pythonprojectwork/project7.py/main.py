import module
import datetime
import time
import random
import uuid
import math
import string
import importlib


# Date and Time
def date_time():
    while True:
        print("\n--- Date and Time ---")
        print("1. Current Date and Time")
        print("2. Difference Between Dates")
        print("3. Custom Date Format")
        print("4. Stopwatch")
        print("5. Countdown")
        print("6. Back")

        ch = input("Enter choice: ")

        if ch == "1":
            print(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

        elif ch == "2":
            try:
                d1 = datetime.date.fromisoformat(input("First date (YYYY-MM-DD): "))
                d2 = datetime.date.fromisoformat(input("Second date (YYYY-MM-DD): "))
                print(f"Difference: {abs((d2-d1).days)} days")
            except ValueError:
                print("Enter valid dates!")

        elif ch == "3":
            print(datetime.datetime.now().strftime("%A, %d %B %Y"))

        elif ch == "4":
            input("Press Enter to start...")
            start = time.time()
            input("Press Enter to stop...")
            print(f"Time: {time.time()-start:.2f} seconds")

        elif ch == "5":
            try:
                seconds = int(input("Enter seconds: "))
                for n in range(seconds, 0, -1):
                    print(n)
                    time.sleep(1)
                print("Time is up!")
            except ValueError:
                print("Enter a valid number!")

        elif ch == "6":
            break

        else:
            print("Invalid choice!")


# Mathematical Operations
def mathematics():
    while True:
        print("\n--- Mathematics ---")
        print("1. Factorial")
        print("2. Compound Interest")
        print("3. Trigonometry")
        print("4. Area of Circle")
        print("5. Back")

        ch = input("Enter choice: ")

        try:
            if ch == "1":
                n = int(input("Enter number: "))
                if n >= 0:
                    print(f"Factorial: {math.factorial(n)}")
                else:
                    print("Number cannot be negative!")

            elif ch == "2":
                p = float(input("Principal: "))
                r = float(input("Rate (%): "))
                t = float(input("Time in years: "))
                amount = p * (1 + r/100) ** t
                print(f"Compound Interest: {amount-p:.2f}")
                print(f"Total Amount: {amount:.2f}")

            elif ch == "3":
                degree = float(input("Enter angle: "))
                radian = math.radians(degree)
                print(f"Sin: {math.sin(radian):.2f}")
                print(f"Cos: {math.cos(radian):.2f}")

            elif ch == "4":
                radius = float(input("Enter radius: "))
                print(f"Circle Area: {math.pi*radius**2:.2f}")

            elif ch == "5":
                break

            else:
                print("Invalid choice!")

        except ValueError:
            print("Please enter a valid number!")


# Random Data
def random_data():
    while True:
        print("\n--- Random Data ---")
        print("1. Random Number")
        print("2. Random List")
        print("3. Random Password")
        print("4. Generate OTP")
        print("5. Back")

        ch = input("Enter choice: ")

        if ch == "1":
            print("Random Number:", random.randint(1, 100))

        elif ch == "2":
            try:
                size = int(input("Enter list size: "))
                if size < 0:
                    print("Size cannot be negative!")
                else:
                    numbers = [random.randint(1, 100) for _ in range(size)]
                    print("Random List:", numbers)
            except ValueError:
                print("Enter a valid size!")

        elif ch == "3":
            try:
                size = int(input("Password length: "))
                if size <= 0:
                    print("Length must be positive!")
                else:
                    chars = string.ascii_letters + string.digits + "!@#$"
                    password = "".join(random.choices(chars, k=size))
                    print(f"Password: {password}")
            except ValueError:
                print("Enter a valid length!")

        elif ch == "4":
            otp = "".join(random.choices(string.digits, k=6))
            print(f"Your OTP: {otp}")

        elif ch == "5":
            break

        else:
            print("Invalid choice!")


# UUID Generator
def generate_uuid():
    print("\nGenerated Unique ID:")
    print(uuid.uuid4())


# File Operations using Module.py
def file_operations():
    while True:
        print("\n--- File Operations ---")
        print("1. Create File")
        print("2. Write File")
        print("3. Read File")
        print("4. Append File")
        print("5. Back")

        ch = input("Enter choice: ")

        if ch == "1":
            name = input("File name: ")
            Module.create_file(name)

        elif ch == "2":
            name = input("File name: ")
            content = input("Enter text: ")
            Module.write_file(name, content)

        elif ch == "3":
            name = input("File name: ")
            Module.read_file(name)

        elif ch == "4":
            name = input("File name: ")
            content = input("Enter text to add: ")
            Module.append_file(name, content)

        elif ch == "5":
            break

        else:
            print("Invalid choice!")


# Explore Module Attributes
def explore_modules():
    name = input("Enter module name (math, random, time): ")

    try:
        module = importlib.import_module(name)
        print(f"\nAttributes of {name}:")
        print(dir(module)[:15])
    except ImportError:
        print("Module not found!")


# Main Menu
def main():
    while True:
        print("\n==============================")
        print("   MULTI-UTILITY TOOLKIT")
        print("==============================")
        print("1. Date and Time")
        print("2. Mathematics")
        print("3. Random Data")
        print("4. Generate UUID")
        print("5. File Operations")
        print("6. Explore Modules")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            date_time()
        elif choice == "2":
            mathematics()
        elif choice == "3":
            random_data()
        elif choice == "4":
            generate_uuid()
        elif choice == "5":
            file_operations()
        elif choice == "6":
            explore_modules()
        elif choice == "7":
            print("Thank you for using the toolkit!")
            break
        else:
            print("Please select from 1 to 7.")


if __name__ == "__main__":
    main()
