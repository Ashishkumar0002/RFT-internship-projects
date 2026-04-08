data = [10, None, 20, 10, "", 30, None, 40]
seen = set()
cleaned = []
removed = 0

for x in data:
    if x in (None, "") or x in seen:
        removed += 1
    else:
        seen.add(x)
        cleaned.append(x)

cleaned.sort()

print(cleaned)
print("Count of removed Values",removed)