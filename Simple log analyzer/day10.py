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
        word = log.split()[0]  # get log type (first word)

        if word in count:
            count[word] += 1

    most = max(count, key=count.get)

    return count, most


counts, most = analyze_logs(logs)

print("Counts:", counts)
print("Most Frequent:", most)
