import numpy as np

employees = [
    ["Omkar", "omkar@gmail.com", 80000],
    ["Parth", "parth@gmail.com", 60000],
    ["Ram", "ram@gmail.com", 55000],
    ["Rahul", "rahul@gmail.com", 70000],
    ["Madhav", "madhav@gmail.com", 45000]
]

print() 

# Salary Array
salaries = np.array([emp[2] for emp in employees])

# Highest Salary
max_salary = np.max(salaries)
max_index = np.argmax(salaries)

print("Highest Salary Employee:")
print(employees[max_index])
print()

# Lowest Salary
min_salary = np.min(salaries)
min_index = np.argmin(salaries)

print("Lowest Salary Employee:")
print(employees[min_index])
print()

# Average Salary
average_salary = np.mean(salaries)

print("Average Salary =", average_salary)  