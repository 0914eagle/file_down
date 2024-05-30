
def total_shares(C, records):
    days = set()
    for company_records in records:
        for record in company_records:
            days.add(record[1])

    total_shares_per_day = {day: 0 for day in days}

    for company_records in records:
        for record in company_records:
            total_shares_per_day[record[1]] += record[0]

    result = [total_shares_per_day[day] for day in sorted(days)]
    return ' '.join(map(str, result))

# Sample Input Parsing
C = int(input())
records = []
for _ in range(C):
    K = int(input())
    company_records = []
    for _ in range(K):
        N, D = map(int, input().split())
        company_records.append((N, D))
    records.append(company_records)

# Call the function with the input
print(total_shares(C, records))
```
