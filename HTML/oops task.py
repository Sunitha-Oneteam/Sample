class Employee:
    def __init__(self,emp_id,emp_name,emp_salary,emp_department):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_salary = emp_salary
        self.emp_department = emp_department

    def get_detials_employee(self):
        self.emp_name = input("Enter your name: ")
        self.emp_id = input("Enter Employee Id: ")
        self.emp_department = input("Enter your Department: ")
        self.emp_salary = input("Enter your Salary: ")

    def calculate_emp_salary(self):
        hours_worked = int(input("Enter Total Working Hours: "))
        overtime = 0
        if hours_worked >= 50:
            overtime = hours_worked - 50
            overtime_amount = (overtime * int(self.emp_salary)/50)
            total_salary = self.emp_salary + str(overtime_amount)
            print("Salary: ",self.emp_salary)
        elif hours_worked < 50:
            print(self.emp_salary)

    def emp_assign_department(self,current_department=""):

            self.emp_department = current_department
            new_department = input("Assigned New Department: ")
            if current_department == self.emp_department:
                self.emp_department = new_department

    def print_employee_details(self):
            print(self.emp_name,self.emp_id,self.emp_department,self.emp_salary)

employee1 = Employee('','','','')
employee1.get_detials_employee()
employee1.calculate_emp_salary()
employee1.emp_assign_department()
employee1.print_employee_details()