def read_csv(file):
    data = []
    
    with open(file, "r") as f:
        next(f)  # skip header
        
        for line in f:
            p, q, pr = line.strip().split(",")
            data.append([p, int(q), int(pr)])
    
    return data


def analyze_sales(data):
    sales = {}
    total_revenue = 0

    for p, q, pr in data:
        total = q * pr
        total_revenue += total
        
        sales[p] = sales.get(p, 0) + total

    top_product = max(sales, key=sales.get)
    sorted_sales = sorted(sales.items(), key=lambda x: x[1], reverse=True)

    return sales, total_revenue, top_product, sorted_sales


# Run
data = read_csv("sales.csv")
sales, revenue, top, sorted_sales = analyze_sales(data)

print("Sales per Product:", sales)
print("Total Revenue:", revenue)
print("Top Product:", top)
print("Sorted Sales:", sorted_sales)
