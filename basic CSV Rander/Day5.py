import csv


def read_csv(file_name):
    data = []

    with open(file_name, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["Age"] = int(row["Age"])
            row["Marks"] = int(row["Marks"])
            data.append(row)

    return data


def average_marks(data):
    return sum(d["Marks"] for d in data) / len(data)


# Run
result = read_csv("students_data_real_names.csv")

print(result)
print("Average Marks:", average_marks(result))
