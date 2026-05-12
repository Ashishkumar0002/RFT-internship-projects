import matplotlib.pyplot as plt
import seaborn as sns

# ---------- READ CSV ----------
data = []

with open("customers.csv", "r") as f:
    next(f)

    for line in f:
        cid, age, spending, visits = line.strip().split(",")

        data.append({
            "ID": cid,
            "AGE": int(age),
            "SPENDING": int(spending),
            "VISITS": int(visits)
        })


# ---------- SEGMENT CUSTOMERS ----------
high = []
medium = []
low = []

for d in data:
    spending = d["SPENDING"]

    if spending >= 1200:
        high.append(d)

    elif spending >= 700:
        medium.append(d)

    else:
        low.append(d)


# ---------- IDENTIFY LOW ENGAGEMENT ----------
low_engagement = [d for d in data if d["VISITS"] <= 4]


# ---------- VISUALIZATION ----------
spending_values = [d["SPENDING"] for d in data]

plt.figure(figsize=(10,5))

# Histogram
plt.subplot(1,2,1)
sns.histplot(spending_values, kde=True)

plt.title("Spending Distribution")


# Pie Chart
labels = ["High", "Medium", "Low"]
sizes = [len(high), len(medium), len(low)]

plt.subplot(1,2,2)
plt.pie(sizes, labels=labels, autopct="%1.1f%%")

plt.title("Customer Categories")

plt.tight_layout()
plt.show()


# ---------- INSIGHTS ----------
print("\n----- CUSTOMER INSIGHTS -----")

print("High Value Customers:", len(high))
print("Medium Value Customers:", len(medium))
print("Low Value Customers:", len(low))

print("\nLow Engagement Users:")
for user in low_engagement:
    print(user["ID"])


# ---------- BUSINESS STRATEGY ----------
print("\n----- BUSINESS STRATEGIES -----")

print("1. Offer loyalty rewards to high-value customers.")
print("2. Send discounts to medium customers.")
print("3. Re-engage low-engagement users with offers.")
