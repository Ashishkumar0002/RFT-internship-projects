data = [
    ["A", "IT", 50000],
    ["B", "HR", 40000],
    ["C", "IT", 60000],
    ["D", "HR", 45000]
]

def analyze_salary(data):
    dept_data = {}

    # Grouping
    for name, dept, salary in data:
        if dept not in dept_data:
            dept_data[dept] = []

        dept_data[dept].append((name, salary))

    avg_salary = {}
    highest_paid = {}
    count_emp = {}

    # Aggregation
    for dept, employees in dept_data.items():
        salaries = [s for _, s in employees]

        avg_salary[dept] = sum(salaries) / len(salaries)
        count_emp[dept] = len(employees)

        # highest paid employee
        highest_paid[dept] = max(employees, key=lambda x: x[1])

    # Sort departments by avg salary
    sorted_dept = sorted(avg_salary.items(), key=lambda x: x[1], reverse=True)

    return avg_salary, highest_paid, count_emp, sorted_dept


avg, high, count, sorted_dept = analyze_salary(data)

print("Average Salary:", avg)
print("Highest Paid:", high)
print("Employee Count:", count)
print("Sorted Departments:", sorted_dept)
