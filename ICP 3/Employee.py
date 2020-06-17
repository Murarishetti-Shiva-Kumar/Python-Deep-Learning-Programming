"""
Create a class Employee and then do the following
	Create a data member to count the number of Employees
	Create a constructor to initialize name, family, salary, department
	Create a function to average salary
	Create a Fulltime Employee class and it should inherit the properties of Employee class
	Create the instances of Fulltime Employee class and Employee class and call their member functions
"""


class Employee:
    Emp_Count = 0  # Data member(class variable)
    Total_Salary = 0

    def __init__(self, name, family, salary, department):  # constructor to initialize name, family, salary, department
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        Employee.Emp_Count += 1
        Employee.Total_Salary += salary
        # return name, family, salary, department, Employee.Emp_Count

    def avg_salary(self):  # function to calculate average salary
        avg_salary = Employee.Total_Salary / Employee.Emp_Count
        return avg_salary


class Full_time_Emp(Employee):  # Full Time Employee class inheriting the Employee class

    def __init__(self, name, family, salary, department, emp_type):
        Employee.__init__(self, name, family, salary, department)
        self.emp_type = emp_type
        # return emp_type


E1 = Employee("shiva", "Murarishetti", 525000, "ICD")
E2 = Employee("Srija", "Nalluri", 375000, "Dev")
E3 = Employee("Tejaswini", "Katteboina", 350000, "Dev")

F1 = Full_time_Emp("shiva", "Murarishetti", 600000, "ML", "Full-Time")
F2 = Full_time_Emp("Srija", "Nalluri", 675000, "Marketing", "Full-Time")
F3 = Full_time_Emp("Tejaswini", "Katteboina", 510000, "Dev-Java", "Contract")

print("Total Number of Employees are:", Employee.Emp_Count)
print("Total Salary given to Employees:", Employee.Total_Salary)
print("Average Salary is:", F3.avg_salary())  # invoking avg_salary function by using the instance
