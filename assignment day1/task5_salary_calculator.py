employee_name = input("Enter employee name: ")
basic_salary = float(input("Enter basic salary: "))

# Calculate allowances
hra = basic_salary * 0.20
da = basic_salary * 0.10
ta = basic_salary * 0.05

# Calculate gross salary
gross_salary = basic_salary + hra + da + ta

# Calculate tax
if gross_salary > 50000:
    tax = gross_salary * 0.10
else:
    tax = 0

# Calculate net salary
net_salary = gross_salary - tax

# Display salary details
print("\n----- Employee Salary Details -----")
print("Employee Name:", employee_name)
print("Basic Salary:", round(basic_salary, 2))
print("HRA:", round(hra, 2))
print("DA:", round(da, 2))
print("TA:", round(ta, 2))
print("Gross Salary:", round(gross_salary, 2))
print("Tax:", round(tax, 2))
print("Net Salary:", round(net_salary, 2))