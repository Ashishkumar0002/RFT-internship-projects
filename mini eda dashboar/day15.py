import matplotlib.pyplot as plt
import seaborn as sns

# ---------- READ CSV ----------
days = []
sales = []

with open("sales_data.csv", "r") as f:
    next(f)

    for line in f:
        d, s = line.strip().split(",")

        days.append(d)
        sales.append(int(s))


# ---------- CREATE SUBPLOTS ----------
fig, ax = plt.subplots(3, 1, figsize=(10, 12))


# ---------- LINE CHART ----------
ax[0].plot(days, sales, marker='o')

ax[0].set_title("Sales Trend")
ax[0].set_xlabel("Days")
ax[0].set_ylabel("Sales")


# ---------- BAR CHART ----------
ax[1].bar(days, sales)

ax[1].set_title("Sales Comparison")
ax[1].set_xlabel("Days")
ax[1].set_ylabel("Sales")


# ---------- HISTOGRAM ----------
sns.histplot(sales, kde=True, ax=ax[2])

ax[2].set_title("Sales Distribution")
ax[2].set_xlabel("Sales")
ax[2].set_ylabel("Frequency")


# ---------- SHOW ----------
plt.tight_layout()
plt.show()


# ---------- INSIGHTS ----------
print("Highest Sales:", max(sales))
print("Lowest Sales:", min(sales))
print("Average Sales:", round(sum(sales)/len(sales), 2))

# Outlier detection
if max(sales) > (sum(sales)/len(sales)) * 1.3:
    print("Possible High Sales Outlier Detected")
