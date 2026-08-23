#OOP-Wrapper

class Person:
    """Represents a basic person with a name and age."""
    def __init__(self, name, age):
        """Initializes a new Person instance.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
        """
        self.name = name
        self.age = age

    def show_details(self):
        """Prints the personal details to the console.

        Returns:
            None
        """
        print("\nPerson Details:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Employee(Person):
    """Represents an employee, inheriting basic traits from Person."""

    def __init__(self, name, age, employee_id, salary):
        """Initializes a new Employee instance.

        Args:
            name (str): The name of the employee.
            age (int): The age of the employee.
            employee_id (str): Unique identity code for the employee.
            salary (float): Total annual or monthly earnings.
        """
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary

    def show_details(self):
        """Prints complete corporate employee details to the console.

        Returns:
            None
        """
        print("\nEmployee Details:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: ${self.salary}")


class Manager(Employee):
    """Represents a company manager, inheriting traits from Employee."""

    def __init__(self, name, age, employee_id, salary, department):
        """Initializes a new Manager instance.

        Args:
            name (str): The name of the manager.
            age (int): The age of the manager.
            employee_id (str): Unique identity code for the manager.
            salary (float): Corporate salary amount.
            department (str): The department overseen by the manager.
        """
        super().__init__(name, age, employee_id, salary)
        self.department = department

    def show_details(self):
        """Prints manager profile and department information to the console.

        Returns:
            None
        """
        print("\nManager Details:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: ${self.salary}")
        print(f"Department: {self.department}")


def main():
    """Runs the console interface loop for managing person, employee, and manager records.

    Returns:
        None
    """

    person = None
    employee = None
    manager = None

    # Matches the exact header from your assignment image
    print("-- Python OOP Project: Employee Management System --")
    
    while True:
        print("\nChoose an operation:")
        print("1. Create a Person")
        print("2. Create an Employee")
        print("3. Create a Manager")
        print("4. Show Details")
        print("5. Exit")
        
        choice = input("\nEnter your choice: ")
        
        if choice == "1":
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            person = Person(name, age)
            print(f"\ Person created with name: {name} and age: {age}.")
            print("\n-- Choose another operation --")
            
        elif choice == "2":
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            employee_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))
            employee = Employee(name, age, employee_id, salary)
            print(f"\nEmployee created with name: {name}, age: {age}, ID: {employee_id}, and salary: ${salary}.")
            print("\n-- Choose another operation --")
            
        elif choice == "3":
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            employee_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))
            department = input("Enter Department: ")
            manager = Manager(name, age, employee_id, salary, department)
            print(f"\nManager created with name: {name}, age: {age}, ID: {employee_id}, salary: ${salary}, and department: {department}.")
            print("\n-- Choose another operation --")
            
        elif choice == "4":
            print("\nChoose details to show:")
            print("1. Person")
            print("2. Employee")
            print("3. Manager")
            details_choice = input("Enter your choice: ")
            
            if details_choice == "1":
                if person is not None:
                    person.show_details()
                else:
                    print("Person has not been created yet.")
            elif details_choice == "2":
                if employee is not None:
                    employee.show_details()
                else:
                    print("Employee has not been created yet.")
            elif details_choice == "3":
                if manager is not None:
                    manager.show_details()
                else:
                    print("Manager has not been created yet.")
            else:
                print("Invalid Choice.")
            print("\n-- Choose another operation --")
                
        elif choice == "5":
            print("Exiting the system. All resources have been freed.")
            print("Goodbye!")
            break
        else:
            print("Invalid input choice.")
            print("\n-- Choose another operation --")


if __name__ == "__main__":
    main()