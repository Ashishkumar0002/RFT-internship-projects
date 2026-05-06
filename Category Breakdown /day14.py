import matplotlib.pyplot as plt

# ---------- READ CSV ----------
data = {}

with open("expenses.csv", "r") as f:
    next(f)  # skip header

    for line in f:
        category, amount = line.strip().split(",")

        amount = int(amount)

        # Group total expense by category
        data[category] = data.get(category, 0) + amount


# ---------- PREPARE DATA ----------
categories = list(data.keys())
expenses = list(data.values())

# Highlight highest category
explode = [0.1 if x == max(expenses) else 0 for x in expenses]


# ---------- PIE CHART ----------
plt.pie(
    expenses,
    labels=categories,
    autopct="%1.1f%%",
    explode=explode
)

plt.title("Expense Category Breakdown")

plt.show()


# ---------- PRINT SUMMARY ----------
print("Total Expenses by Category:")
for c, e in data.items():
    print(c, ":", e)
