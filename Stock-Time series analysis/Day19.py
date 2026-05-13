import matplotlib.pyplot as plt

# ---------- READ CSV ----------
dates = []
prices = []

with open("stock_data.csv", "r") as f:
    next(f)

    for line in f:
        date, price = line.strip().split(",")

        dates.append(date)
        prices.append(int(price))


# ---------- MOVING AVERAGE ----------
moving_avg = []

window = 3

for i in range(len(prices)):
    if i < window - 1:
        moving_avg.append(None)
    else:
        avg = sum(prices[i-window+1:i+1]) / window
        moving_avg.append(avg)


# ---------- PEAKS & DROPS ----------
highest = max(prices)
lowest = min(prices)

high_day = dates[prices.index(highest)]
low_day = dates[prices.index(lowest)]


# ---------- VOLATILITY ----------
volatility = max(prices) - min(prices)


# ---------- VISUALIZATION ----------
plt.figure(figsize=(10,5))

# Stock price trend
plt.plot(dates, prices,
         marker='o',
         label="Stock Price")

# Moving average line
plt.plot(dates, moving_avg,
         linestyle='--',
         label="Moving Average")

plt.xticks(rotation=45)

plt.title("Stock Price Analysis")
plt.xlabel("Date")
plt.ylabel("Price")

plt.legend()
plt.grid()

plt.show()


# ---------- INSIGHTS ----------
print("\n----- STOCK INSIGHTS -----")

print("Highest Price:", highest, "on", high_day)

print("Lowest Price:", lowest, "on", low_day)

print("Volatility:", volatility)

print("Average Price:",
      round(sum(prices)/len(prices), 2))
