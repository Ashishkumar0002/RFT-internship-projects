import matplotlib.pyplot as plt
import seaborn as sns

# ---------- READ CSV ----------
data = []

with open("sales_eda.csv", "r") as f:
    next(f)

    for line in f:
        date, product, region, sales = line.strip().split(",")

        # Handle missing values
        if sales == "":
            continue

        data.append({
            "DATE": date,
            "PRODUCT": product,
            "REGION": region,
            "SALES": int(sales)
        })


# ---------- AGGREGATION ----------
product_sales = {}
region_sales = {}
dates = []
sales_values = []

for d in data:
    product = d["PRODUCT"]
    region = d["REGION"]
    sales = d["SALES"]

    product_sales[product] = product_sales.get(product, 0) + sales
    region_sales[region] = region_sales.get(region, 0) + sales

    dates.append(d["DATE"])
    sales_values.append(sales)


# ---------- SUBPLOTS ----------
fig, ax = plt.subplots(2, 1, figsize=(10, 10))


# ---------- LINE CHART ----------
ax[0].plot(dates, sales_values, marker='o')

ax[0].set_title("Sales Trend")
ax[0].set_xlabel("Date")
ax[0].set_ylabel("Sales")
ax[0].tick_params(axis='x', rotation=45)


# ---------- BAR CHART ----------
ax[1].bar(product_sales.keys(), product_sales.values())

ax[1].set_title("Total Sales per Product")
ax[1].set_xlabel("Product")
ax[1].set_ylabel("Sales")


plt.tight_layout()
plt.show()


# ---------- INSIGHTS ----------
print("\n----- KEY INSIGHTS -----")

print("Top Product:",
      max(product_sales, key=product_sales.get))

print("Best Region:",
      max(region_sales, key=region_sales.get))

print("Total Revenue:",
      sum(sales_values))

print("Average Sales:",
      round(sum(sales_values) / len(sales_values), 2))

# Monthly growth analysis
growth = sales_values[-1] - sales_values[0]

print("Growth from Start to End:", growth)
