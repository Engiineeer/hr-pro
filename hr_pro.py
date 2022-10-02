class Employee:
    def __init__(self,name,age,salary,employment_years):
        self.name=name
        self.age=age
        self.salary=salary
        self.employment_years=employment_years


    def __str__(self):
        return  f"Name: {self.name}, age:{self.age}, Salary:{self.salary}, Working Years: {self.employment_years}"

    def get_annual_salary(self):
        return self.salary*12



class Manager(Employee):
    def __init__(self, name, age, salary, employment_years,bonus_percentage):
         super().__init__(name, age, salary, employment_years)
         self.bonus_percentage=bonus_percentage

    def __str__(self):
        return  f"Name: {self.name}, age:{self.age}, Salary:{self.salary}, Working Years: {self.employment_years}, Bonus: {self.bonus_percentage}"

    def get_bonus(self,bonus_percentage):
        return bonus_percentage*self.salary

n=1        
while n>0:
    employee_one = Employee("Laila",24,9999,4)
    employee_two = Employee("Moh",27,999,2)
    manager_one = Manager("sammy",52,4600,19,1380.0)
    employee_list = [employee_one,employee_two]
    manager_list = [manager_one]

    print("Welcome to HR Pro\nOptions: \n   1. Show Employees\n   2. Show Managers\n   3. Add An Employee\n   4. Add A Manager\n   5. Exit\n\n")
    the_input = int(input("What would you like to do? "))
    if the_input == 1:
        print("-----------------\nEmployees\n\n")
        for emp in employee_list:
            print(emp)

    elif the_input == 2:
        print("-----------------\Managers\n\n")
        for mang in manager_list:
            print(mang)

    elif the_input == 3:
        print("-----------------\n")
        employee_list.append(Employee(input("name: "),int(input("Age: ")),int(input("Salary: ")),int(input("Employement years: "))))
        
        print("Employee added succesfully\n")
        for emp in employee_list:
            print(emp)
    elif the_input == 4:
        print("-----------------\n")
        manager_list.append(Manager(input("name: "),int(input("Age: ")),int(input("Salary: ")),int(input("Employement years: ")),float(input("Bonus Percentage: "))))
        
        print("Manager  added succesfully\n")
        for mang in manager_list:
            print(mang)

    elif the_input == 5:
        break
