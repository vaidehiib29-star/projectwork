#Employee Management System
#Parent Class

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Person Deatils:")
        print("Name:", self.name)
        print("Age:", self.age)

#Employee Class

class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)

        #private
        self.__employee_id = employee_id
        self.__salary = salary

        #Getter Employee id
        def get_employee_id(self):
            return self.__employee_id

        #setter Employee id
        def set_employee_id(self, employee_id):
            self.__employee_id = employee_id

        #Getter Salary
        def get_salary(self):
            return self.__salary

        #Setter Salary
        def set_salary(self, salary):
            self.__salary = salary

            
