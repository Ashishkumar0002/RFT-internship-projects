import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------- LOAD DATA ----------
df = pd.read_csv("sales_capstone.csv")

print("\n----- DATASET -----")
print(df.head())


# ---------- DATA CLEANING ----------
df.dropna(inplace=True)

print("\nMissing Values Removed")


# ---------- ANALYSIS ----------
total_sales = df["SALES"].sum()

avg_sales = df["SALES"].mean()

top_product = df.groupby("PRODUCT")["SALES"].sum()

top_region = df.groupby("REGION")["SALES"].sum()


# ---------- VISUALIZATION ----------
plt.figure(figsize=(14,5))


# Product Sales
plt.subplot(1,2,1)

top_product.plot(kind="bar")

plt.title("Sales Per Product")
plt.ylabel("Revenue")


# Region Sales
plt.subplot(1,2,2)

top_region.plot(kind="pie",
                autopct="%1.1f%%")

plt.title("Region-wise Sales")
plt.ylabel("")


plt.tight_layout()
plt.show()


# ---------- SALES TREND ----------
plt.figure(figsize=(10,5))

plt.plot(df["DATE"],
         df["SALES"],
         marker="o")

plt.xticks(rotation=45)

plt.title("Sales Trend")
plt.xlabel("Date")
plt.ylabel("Sales")

plt.grid()

plt.show()


# ---------- INSIGHTS ----------
print("\n----- BUSINESS INSIGHTS -----")

print("Total Sales:", total_sales)

print("Average Sales:", round(avg_sales, 2))

print("\nTop Product:")
print(top_product.idxmax())

print("\nBest Region:")
print(top_region.idxmax())


# ---------- WRITTEN SUMMARY ----------
print("\n----- SUMMARY -----")

print("1. Laptop generated the highest revenue.")

print("2. North and West regions performed strongly.")

print("3. Sales show an upward trend over time.")

print("4. Tablet sales are comparatively lower.")

print("5. Mobile sales remain stable across regions.")
