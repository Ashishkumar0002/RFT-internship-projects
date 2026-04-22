import matplotlib.pyplot as plt

dates = ["MON", "TUE", "WED", "THU", "FRI"]
sales = [200, 250, 300, 280, 350]

# Find highest & lowest
max_sale = max(sales)
min_sale = min(sales)

max_day = dates[sales.index(max_sale)]
min_day = dates[sales.index(min_sale)]

# Plot line chart
plt.plot(dates, sales, marker='o')

# Highlight highest point
plt.scatter([max_day], [max_sale], color='green', zorder=5)
plt.text(max_day, max_sale + 5, f"High: {max_sale}", color='green')

# Highlight lowest point
plt.scatter([min_day], [min_sale], color='red', zorder=5)
plt.text(min_day, min_sale - 15, f"Low: {min_sale}", color='red')

# Labels & title
plt.title("Sales Trend (Mon–Fri)")
plt.xlabel("Days")
plt.ylabel("Sales")

plt.grid()
plt.show()
