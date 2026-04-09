marks = [78, 85, 90, 67, 85, 92, 78]

def analyze(marks):
    avg = sum(marks) / len(marks)
    
    return {
        "Average": avg,
        "Highest": max(marks),
        "Lowest": min(marks),
        "Above Avg": sum(1 for m in marks if m > avg),
        "Grades": {
            "A": sum(1 for m in marks if m >= 90),
            "B": sum(1 for m in marks if 75 <= m < 90),
            "C": sum(1 for m in marks if 50 <= m < 75),
            "F": sum(1 for m in marks if m < 50),
        }
    }

result = analyze(marks)

for k, v in result.items():
    print(k, ":", v)
