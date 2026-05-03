import matplotlib.pyplot as plt

# ---------- READ CSV ----------
def read_csv(file):
    data = []
    with open(file, "r") as f:
        next(f)
        for line in f:
            name, m, s, e = line.strip().split(",")
            data.append({
                "NAME": name,
                "MATHS": int(m),
                "SCIENCE": int(s),
                "ENGLISH": int(e)
            })
    return data


# ---------- ANALYSIS ----------
def analyze(data):
    total_avg = 0

    for d in data:
        avg = (d["MATHS"] + d["SCIENCE"] + d["ENGLISH"]) / 3
        d["AVG"] = avg
        total_avg += avg

    overall_avg = total_avg / len(data)

    topper = max(data, key=lambda x: x["AVG"])

    return overall_avg, topper


# ---------- VISUALIZATION ----------
def plot_top_students(data):
    # Take top 5 students
    top5 = sorted(data, key=lambda x: x["AVG"], reverse=True)[:5]

    names = [d["NAME"] for d in top5]
    avgs = [d["AVG"] for d in top5]

    plt.bar(names, avgs)

    # Add labels
    for i, v in enumerate(avgs):
        plt.text(i, v, str(round(v, 1)), ha='center')

    plt.title("Top 5 Students (Average Marks)")
    plt.xlabel("Students")
    plt.ylabel("Average Marks")

    plt.show()


# ---------- MAIN ----------
students = read_csv("students.csv")

overall_avg, topper = analyze(students)

print("Overall Average:", round(overall_avg, 2))
print("Topper:", topper["NAME"], "with avg:", round(topper["AVG"], 2))

plot_top_students(students)
