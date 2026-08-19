# Employee Management System
class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.__salary = salary 

    # Get Salary
    def get_salary(self):
        return self.__salary

    # Set Salary
    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
            print("Salary updated successfully")
        else:
            print("Invalid salary")

    # Display Employee Information
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: {self.__salary}")

    # Work method
    def work(self):
        print(f"Name: {self.name} is working....")


# Single Inheritance - Developer Class
class Developer(Employee):
    def __init__(self, name, employee_id, salary, programming_language):
        super().__init__(name, employee_id, salary)
        self.programming_language = programming_language

    def work(self):
        print(f"{self.name} is writing code in {self.programming_language}")

    def display_info(self):
        super().display_info()
        print(f"Programming Language: {self.programming_language}")


# Hierarchical Inheritance - Manager Class
class Manager(Employee):
    def __init__(self, name, employee_id, salary, team_size):
        super().__init__(name, employee_id, salary)
        self.team_size = team_size

    def work(self):
        print(f"{self.name} is managing a team of {self.team_size} people")

    def display_info(self):
        super().display_info()
        print(f"Team Size: {self.team_size}")


# Trainer Class
class Trainer:
    def __init__(self, expertise):
        self.expertise = expertise

    def conduct_training(self):
        print(f"Conducting training on {self.expertise}")

    def work(self):
        print(f"Trainer is working on {self.expertise}")


# Multiple and Multilevel Inheritance
class SeniorDeveloper(Developer, Trainer):
    def __init__(self, name, employee_id, salary, programming_language, expertise, years_of_expertise):
        Developer.__init__(self, name, employee_id, salary, programming_language)
        Trainer.__init__(self, expertise)
        self.years_of_expertise = years_of_expertise

    # Method Overriding
    def work(self):
        print(f"{self.name} is architecting systems and mentoring developers")

    def display_info(self):
        super().display_info()
        print(f"Expertise: {self.expertise}")
        print(f"Years of Expertise: {self.years_of_expertise}")


# --- Execution ---

print("---------Employee---------")
employee = Employee("vaidehi", "E101", 30000)
employee.display_info()
employee.work()

print("\nChanging Salary:")
employee.set_salary(35000)
print("New Salary:", employee.get_salary())

print("\n---------Developer-------")
dev = Developer("Jay", "D102", 50000, "Python")
dev.display_info()
dev.work()

print("\n-----------Manager--------")
mgr = Manager("Het", "M103", 70000, 10)
mgr.display_info()
mgr.work()

print("\n--------Senior Developer-------")
senior = SeniorDeveloper(
    "Kano", "S104", 90000, "Python", "Machine Learning", 8
)
senior.display_info()
senior.work()

print("\nTraining:")
senior.conduct_training()

print("\n--------Polymorphism---------")
# Using the correct variable names defined above
employees = [employee, dev, mgr, senior] 
for e in employees:
    e.work()

print("\n------Display Information--------")
for e in employees:
    e.display_info()
    print()

print("-------MRO------")
for cls in SeniorDeveloper.mro():
    print(cls.__name__)

print("\n---------Inheritance Check------")
print("Is Manager subclass of Employee?", issubclass(Manager, Employee))
print("Is SeniorDeveloper subclass of Developer?", issubclass(SeniorDeveloper, Developer))
print("Is SeniorDeveloper subclass of Employee?", issubclass(SeniorDeveloper, Employee))
print("Is SeniorDeveloper subclass of Trainer?", issubclass(SeniorDeveloper, Trainer))

