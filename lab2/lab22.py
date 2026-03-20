#2
import csv
def load_employees(filename):
    employees = []
    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["salary"] = int(row["salary"])
            employees.append(row)
    return employees
def average_salary(employees):
    total = sum(emp["salary"] for emp in employees)
    return total / len(employees)
def department_average(employees):
    departments = {}

    for emp in employees:
        dept = emp["department"]
        departments.setdefault(dept, []).append(emp["salary"])
    result = {}
    for dept, salaries in departments.items():
        result[dept] = sum(salaries) / len(salaries)
    return result
def high_salary(employees, avg):
    return [emp for emp in employees if emp["salary"] > avg]
employees = load_employees("employees.csv")
avg = average_salary(employees)
dept_avg = department_average(employees)
high = high_salary(employees, avg)
print("Орташа зарплата:", avg)
print("Бөлім бойынша:", dept_avg)
print("Жоғары зарплата:", high)