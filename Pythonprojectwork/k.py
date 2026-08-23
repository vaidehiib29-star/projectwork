# OOP Wraper

class Person:
    '''
    A class to represent a person.
    
    Attributes:
    name(str): The name of the person
    age(int): The age of the person
    '''
    def __init__(self,name,age):
        '''
        Intializes the person object with a name and age.
        Returns: None
        '''
        self.name = name
        self.age = age

    def display(self):
        '''
        Prints the person's name and age
        Returns:
        None
        '''
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

    def __del__(self):
        '''
        Deconstructor method called when an object is deleted.
        Returns: None
        '''
        pass


class Employee(Person):
    '''
    A class to represent an employee, inheriting basic attributes from person.
    Attributes:
        __employee_id(str): Private string identifying the employee.
        __salary(float): Private decimal tracking the employee's salary.
    '''
    def __init__(self,*args):
        '''
        Initializes an employee dynamically based on argument count.
        Parameter:
        *args : Can be (name,age,employee_id,salary) or (name,age).

        Returns: None
        '''
        if len(args) == 4:
            super().__init__(args[0],args[1])
            self.__employee_id = args[2]
            self.__salary = float(args[3])

        elif len(args) == 2:
            super().__init__(args[0],args[1])
            self.__employee_id = "Not_Assigned"
            self.__salary = 0.0

        else:
            super().__init__("Unknown",0)
            self.__employee_id = "Unknown"
            self.__salary = 0.0

    def get_employee_id(self):
        '''
        Getter: Access the private employee ID.
        Returns: 
        The private employee ID string value.
        '''
        return self.__employee_id

    def set_employee_id(self,employee_id):
        '''
        Setter: Update the private employee ID value.
        Returns: None
        '''
        self.__employee_id = employee_id

    def get_salary(self):
        '''
        Getter: Access the private salary.
        Returns:
        The private salary decimal value.
        '''
        return self.__salary

    def set_salary(self,salary):
        '''
        Setter: Safely updates the private salary value.
                Validates that the input is non negative before applying changes.
        Returns: None
        '''
        if salary >= 0:
            self.__salary = float(salary)
        else:
            print("Error: Salary cannot be negative.")

    def display(self):
        '''
        Polimorphic display function.
        Calls parent display and adds employee data.
        Returns: None
        '''
        super().display()
        print(f"Employee ID: {self.get_employee_id()}")
        print(f"Salary: ₹{self.get_salary() :.2f}")

class Manager(Employee):
    '''
    A class to represent a Manager , inheriting from Employee.
    Attributes:
        department(str): The department the manager handles.
    '''
    def __init__(self,name,age,employee_id,salary,department):
        '''
        Intializes a Manager instance.
        Parameters:
            name(str): Name of the manager.
            age(int): Age of the manager.
            employee_id: Enterrise employee ID.
            salary(float): Assigned Salary.
            department(str): Assigned active management branch.
        Returns: None
        '''
        super().__init__(name,age,employee_id,salary)
        self.department = department

    def display(self):
        '''
        Polymorphic display function.
        Adds employee data with department.
        Returns: None
        '''
        super().display()
        print(f"Department: {self.department}")

class Developer(Employee):
    '''
    A class to represent a Developer, inheriting from Employee.
    Attributes:
        programming_language(str): The primary code language used by the developer.
    '''
    def __init__(self,name,age,employee_id,salary,programming_language):
        '''
        Intializes a Developer instance.
        Parameters:
            name(str): Name of the developer.
            age(int): Age of the developer.
            employee_id(str): Enterprise employee ID.
            salary(float):Assigned salary.
            programming_language(str):Core programming language tool used by developer.
        Returns: None
        '''
        super().__init__(name,age,employee_id,salary)
        self.programming_language =programming_language

    def display(self):
        '''
        Polymorphic display function.
        Adds employee data with programming Language used.
        Returns: None
        '''
        super().display()
        print(f"Programming Language: {self.programming_language}")

def main():
    '''
    The main driver function running the command-line interface.
    Manages an exection loop allowing users to provision instances of person,employee,manager,and developer,and print active information.
    Returns:None
    '''
    instance = {
        "Person" : None,
        "Employee" : None,
        "Manager" : None,
        "Developer" : None
        }
    print("--- Python OOP Project: Employee Management System ---")
    while True:
    
        print("Choose an Operation: ")
        print("1.Create a Person")
        print("2.Create an Employee")
        print("3.Create a Manager")
        print("4.Create a Developer")
        print("5.Show Details")
        print("6.Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            instance["Person"] = Person(name,age)
            print(f"Person created with name: {instance['Person'].name} and age: {instance['Person'].age}.")
            print("--- Choose another operation ---")

        elif choice == "2":
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            emp_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))
            instance["Employee"] = Employee(name,age,emp_id,salary)
            print(f"Employee created with name: {instance['Employee'].name},age: {instance['Employee'].age},ID: {instance['Employee'].get_employee_id()},and Salary: ₹{instance['Employee'].get_salary():.2f}.")
            print("--- Choose another operation ---")

        elif choice == "3":
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            emp_id = input("Enter employee ID: ")
            salary = float(input("Enter salary: "))
            dep = input("Enter Department: ")
            instance["Manager"] = Manager(name,age,emp_id,salary,dep)
            print(f"Manager created with name: {instance['Manager'].name},age: {instance['Manager'].age},ID: {instance['Manager'].get_employee_id()},Salary: {instance['Manager'].get_salary():.2f},and Department: {instance['Manager'].department}.")
            print("--- Choose another operation ---")
        elif choice == "4":
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            emp_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))
            language = input("Enter Progrmming Language: ")
            instance["Developer"] = Developer(name,age,emp_id,salary,language)
            print(f"Developer create with name: {instance['Developer'].name},age: {instance['Developer'].age},ID: {instance['Developer'].get_employee_id()},Salary: {instance['Developer'].get_salary():.2f},and Programming Language: {instance['Developer'].programming_language}.")
            print("--- Choose another Operation ---")

        elif choice == "5":
            print("Choose details to show: ")
            print("1. Person")
            print("2.Employee")
            print("3.Manager")
            print("4.Developer")
            subchoice = input("Enter your choice: ")

            if subchoice == "1":
                if instance["Person"]:
                    print("Person Details: ")
                    instance["Person"].display()
                else:
                    print("No Person object has been created yet.")

            elif subchoice == "2":
                if issubclass(Employee,Person):
                    if instance["Employee"]:
                        print("Employee Details:")
                        instance["Employee"].display()
                    else:
                        print("No Employee object is created yet.")
                else:
                    print("Erroe: Employee is not a subclass of Person!")

            elif subchoice == "3":
                if issubclass(Manager,Employee):
                    if instance["Manager"]:
                        print("Manager Details: ")
                        instance['Manager'].display()
                    else:
                        print("No Manager object has been created yet.")
                else:
                    print("Error: Manager is not subclass of Employee!")

            elif subchoice == "4":
                if issubclass(Developer,Employee):
                    if instance["Developer"]:
                        print("Developer Details: ")
                        instance["Developer"].display()
                    else:
                        print("No Developer object has been created yet.")
                else:
                    print("Error: Developer is not a subclass of Employee!")
                    
            else:
                print("Invalid Choice.")
                print("--- Choose another operation ---")

        elif choice == "6":
                instance.clear()
                print("Exiting the system. All resources have been freed")
                print("Goodbye!")
                break
        else:
                print("Invalid input choice.")

if __name__ == "__main__":
    main()