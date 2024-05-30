
def total_shares_held(C, records):
    shares_by_day = {}
    for company_records in records:
        for shares, day in company_records:
            if day in shares_by_day:
                shares_by_day[day] += shares
            else:
                shares_by_day[day] = shares

    sorted_days = sorted(shares_by_day.keys())
    result = [shares_by_day[day] for day in sorted_days]
    return " ".join(map(str, result))

# Parse input
C = int(input())
records = []
for _ in range(C):
    K = int(input())
    company_records = []
    for _ in range(K):
        shares, day = map(int, input().split())
        company_records.append((shares, day))
    records.append(company_records)

# Call the function and print the result
print(total_shares_held(C, records))
```
