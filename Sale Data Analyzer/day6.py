data = [
    ["A", 2, 100],
    ["B", 1, 200],
    ["A", 3, 100],
    ["C", 5, 50]
]

def analyze_sales(data):
    sales = {}
    total_revenue = 0

    for product, qty, price in data:
        total = qty * price  # bonus column
        
        total_revenue += total
        
        if product in sales:
            sales[product] += total
        else:
            sales[product] = total

    # Top selling product
    top_product = max(sales, key=sales.get)

    # Sort by revenue (bonus)
    sorted_sales = sorted(sales.items(), key=lambda x: x[1], reverse=True)

    return sales, total_revenue, top_product, sorted_sales


sales, revenue, top, sorted_sales = analyze_sales(data)

print("Sales per Product:", sales)
print("Total Revenue:", revenue)
print("Top Product:", top)
print("Sorted Sales:", sorted_sales)
