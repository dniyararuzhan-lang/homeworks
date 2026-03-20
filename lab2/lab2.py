
#2
import csv
def load_employees(file):
    with open(file, encoding="utf-8") as f:
        employees = list(csv.DictReader(f))
        for e in employees:
            e["salary"] = int(e["salary"])
        return employees
def average_salary(employees):
    return sum(e["salary"] for e in employees) / len(employees)
def department_average(employees):
    departments = {}   # ✅ дұрыс атау
    for emp in employees:
        dept = emp["position"]   # ✅ тек мән алу
        departments.setdefault(dept, []).append(emp["salary"])
    return {d: sum(s) / len(s) for d, s in departments.items()}
def high_salary(employees, avg):
    return [e for e in employees if e["salary"] > avg]
employees = load_employees("/Users/aruzhan/PyCharmMiscProject/lab2/employees.csv")
avg = average_salary(employees)
print("Орташа", avg)
print("бөлім", department_average(employees))
print("жоғары", high_salary(employees, avg))
#1
with open("data.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
users = set()
total_purchases = 0
total_sum = 0
user_spending = {}
for line in lines:
    p = line.strip().split()
    if len(p) < 3:
        continue
    user = p[1]
    action = p[2]
    users.add(user)
    if action == "BUY" and len(p) > 3:
        amount = int(p[3])
        total_purchases += 1
        total_sum += amount
        user_spending[user] = user_spending.get(user, 0) + amount
max_user = max(user_spending, key=user_spending.get) if user_spending else None
average = total_sum / total_purchases if total_purchases > 0 else 0
print("Сумма:", total_sum)
print("Users:", len(users))
print("Покупки:", total_purchases)
print("Топ user:", max_user)
print("Средний:", average)
#4
import csv
import json
def load_transactions(filename):
    transactions = []
    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["amount"] = int(row["amount"])
            transactions.append(row)
    return transactions
def analyze(transactions):
    suspicious_transactions = []
    user_counts = {}
    for t in transactions:
        if t["amount"] > 500000:
            suspicious_transactions.append(t)
        user = t["user_id"]
        user_counts[user] = user_counts.get(user, 0) + 1
    suspicious_users = {u for u, c in user_counts.items() if c > 3}
    total = sum(t["amount"] for t in suspicious_transactions)
    return suspicious_transactions, suspicious_users, total
transactions = load_transactions("transactions.csv")
sus_t, sus_u, total = analyze(transactions)
print("Күдікті транзакция:", sus_t)
print("Күдікті user:", sus_u)
print("Жалпы сумма:", total)
#3
import json
def load_orders(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
def total_revenue(orders):
    return sum(order["total"] for order in orders)
def user_orders(orders):
    result = {}
    for order in orders:
        user = order["user"]
        result[user] = result.get(user, 0) + 1
    return result
def most_popular_item(orders):
    items = {}
    for order in orders:
        for item in order["items"]:
            items[item] = items.get(item, 0) + 1
    return max(items, key=items.get)
orders = load_orders("orders.json")
print("Барлық табыс:", total_revenue(orders))
print("User заказ саны:", user_orders(orders))
print("Популярный товар:", most_popular_item(orders))
