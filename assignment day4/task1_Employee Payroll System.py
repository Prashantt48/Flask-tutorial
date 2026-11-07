
# Assignment 4 - Task 1: Employee Payroll System



class Employee:
    def __init__(self, emp_id, name, base_salary):
        self.emp_id = emp_id
        self.name = name
        self.base_salary = base_salary

    def get_salary(self):
        return self.base_salary

    def __str__(self):
        return (
            f"ID: {self.emp_id}, Name: {self.name}, "
            f"Salary: Rs.{self.get_salary():.2f}"
        )



class FullTimeEmployee(Employee):
    def get_salary(self):
        # Full-time employees receive a 20% bonus
        return self.base_salary * 1.20



class PartTimeEmployee(Employee):
    def __init__(self, emp_id, name, hours_worked, rate_per_hour):
        super().__init__(emp_id, name, 0)
        self.hours_worked = hours_worked
        self.rate_per_hour = rate_per_hour

    def get_salary(self):
        return self.hours_worked * self.rate_per_hour

    def __str__(self):
        return (
            f"ID: {self.emp_id}, Name: {self.name}, "
            f"Hours: {self.hours_worked}, "
            f"Rate/hour: Rs.{self.rate_per_hour:.2f}, "
            f"Salary: Rs.{self.get_salary():.2f}"
        )



employees = []



def add_full_time_employee():
    emp_id = input("Enter employee ID: ")
    name = input("Enter employee name: ")
    base_salary = float(input("Enter base salary: "))

    employee = FullTimeEmployee(emp_id, name, base_salary)
    employees.append(employee)

    print("Full-time employee added successfully!")



def add_part_time_employee():
    emp_id = input("Enter employee ID: ")
    name = input("Enter employee name: ")
    hours = float(input("Enter hours worked: "))
    rate = float(input("Enter rate per hour: "))

    employee = PartTimeEmployee(emp_id, name, hours, rate)
    employees.append(employee)

    print("Part-time employee added successfully!")



def display_employees():
    if not employees:
        print("No employees found.")
        return

    print("\n========== EMPLOYEE DETAILS ==========")

    for employee in employees:
        print(employee)



def display_payroll_report():
    if not employees:
        print("No employees available for payroll.")
        return

    total_payroll = sum(map(lambda emp: emp.get_salary(), employees))

    print("\n========== PAYROLL REPORT ==========")

    for employee in employees:
        print(f"{employee.name}: Rs.{employee.get_salary():.2f}")

    print(f"Total payroll: Rs.{total_payroll:.2f}")

    threshold = float(input("Enter salary threshold: "))

    high_salary_employees = list(
        filter(lambda emp: emp.get_salary() > threshold, employees)
    )

    print(f"\nEmployees earning above Rs.{threshold:.2f}:")

    if high_salary_employees:
        for employee in high_salary_employees:
            print(employee)
    else:
        print("No employees found above this threshold.")



def apply_bonus():
    if not employees:
        print("No employees available.")
        return

    # Calculate adjusted salaries without changing original salaries
    bonus_salaries = list(
        map(lambda emp: emp.get_salary() * 1.10, employees)
    )

    print("\n========== SALARIES WITH 10% BONUS ==========")

    for employee, new_salary in zip(employees, bonus_salaries):
        print(
            f"{employee.name}: Original Rs.{employee.get_salary():.2f}, "
            f"With bonus Rs.{new_salary:.2f}"
        )



def main():
    while True:
        print("\n========== EMPLOYEE PAYROLL SYSTEM ==========")
        print("1. Add Full Time Employee")
        print("2. Add Part Time Employee")
        print("3. Display All Employees")
        print("4. Display Payroll Report")
        print("5. Apply Bonus (Lambda)")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_full_time_employee()

        elif choice == "2":
            add_part_time_employee()

        elif choice == "3":
            display_employees()

        elif choice == "4":
            display_payroll_report()

        elif choice == "5":
            apply_bonus()

        elif choice == "6":
            print("Thank you for using the Payroll System!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
