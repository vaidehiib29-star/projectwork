class Employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary < 0:
            print("Salary can not be negative")
        else:
            self.__salary = salary
            print("salary updated")

    def display(self):
        print("ID:", self.id)
        print("Name:", self.name)
        print("Salary:", self.__salary)

class Developer(Employee):

    def __init__(self, id, name, salary, language, experience):
        super().__init__(id, name, salary)

        self.language = language
        self.experience = experience

    def display(self):
        super().display()
        print("Language:", self.language)


class Developer(Employee):

    def __init__(self, id, name, salary, language, experience):
        super().__init__(id, name, salary)
        self.language = language
        self.experience = experience

    def display(self):
        super().display()
        print("Language:", self.language)
        print("Experience:", self.experience)


class Manager(Employee):
    def __init__(self, id, name, salary, department, team):
        super().__init__(id, name, salary)
        self.department = department
        self.team = team

    def display(self):
        super().display()
        print("Department:", self.department)
        print("Team Size:", self.team)


class TechnicalSkills:

    def __init__(self, skill, certificate):
        self.skill = skill
        self.certificate = certificate

    def show_skill(self):
        print("Skill:", self.skill)
        print("Certificate:", self.certificate)


class TechLead(Developer, TechnicalSkills):

    def __init__(self, id, name, salary, language, experience, skill, certificate):

        Developer.__init__(self, id, name, salary, language, experience)

        TechnicalSkills.__init__(self, skill, certificate)

    def display(self):
        Developer.display(self)
        self.show_skill()


#-----Employee------
print("\nEmployee Details")

e1 = Employee(1, "vaidehi", 30000)
e1.display()

#------Developer-----
print("\nDeveloper Details")

d1 = Developer(2, "Jay", 45000, "Python", 2)
d1.display()

#------Manager------
print("\nManager Details")

m1 = Manager(3, "Het", 60000, "IT", 3)
m1.display()

#----Tech-Lead----
print("\nTech Lead Details")

t1 = TechLead(4, "Shivu", 40000, "Python", 5, "Cloud", "AWS")
t1.display()

#------Getter-----
print("\nSalary using Getter")
print(e1.get_salary())

#-------Setter----
print("\nChanging Salary")
e1.set_salary(35000)
print("New Salary:", e1.get_salary())

#-----Negative Slary----
print("\nTesting Negative Salary")
e1.set_salary(-10000)

