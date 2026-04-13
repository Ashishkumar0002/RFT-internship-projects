logs = [
    "ERROR DISK FULL",
    "INFO STARTED",
    "ERROR FILE MISSING",
    "WARNING MEMORY LOW"
]

def analyze_logs(logs):
    count = {"ERROR": 0, "INFO": 0, "WARNING": 0}

    for log in logs:
        log = log.upper()  # ignore case
        for key in count:
            if key in log:
                count[key] += 1

    # Most frequent log type
    most_frequent = max(count, key=count.get)

    return count, most_frequent


counts, most = analyze_logs(logs)

print("Counts:", counts)
print("Most Frequent:", most)
