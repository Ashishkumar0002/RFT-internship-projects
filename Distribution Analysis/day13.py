import seaborn as sns
import matplotlib.pyplot as plt

# ---------- READ CSV ----------
def read_csv(file):
    data = []
    with open(file, "r") as f:
        next(f)
        for line in f:
            name, m, s, e = line.strip().split(",")
            avg = (int(m) + int(s) + int(e)) / 3
            data.append(avg)
    return data


# ---------- LOAD DATA ----------
marks = read_csv("students.csv")


# ---------- PLOT ----------
sns.histplot(marks, kde=True)

plt.title("Distribution of Student Average Marks")
plt.xlabel("Average Marks")
plt.ylabel("Frequency")

plt.show()


# ---------- SKEWNESS ----------
mean = sum(marks) / len(marks)
median = sorted(marks)[len(marks)//2]

print("Mean:", round(mean, 2))
print("Median:", round(median, 2))

if mean > median:
    print("Right Skewed (Positive Skew)")
elif mean < median:
    print("Left Skewed (Negative Skew)")
else:
    print("Symmetrical Distribution")
