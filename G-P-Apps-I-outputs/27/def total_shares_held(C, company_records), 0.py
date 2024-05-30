
def total_shares_held(C, company_records):
    day_shares = {}
    for records in company_records:
        for shares, day in records:
            if day in day_shares:
                day_shares[day] += shares
            else:
                day_shares[day] = shares
                
    sorted_days = sorted(day_shares.keys())
    result = [day_shares[day] for day in sorted_days]
    return ' '.join(map(str, result))

# Read input
C = int(input())
company_records = []
for _ in range(C):
    K = int(input())
    records = []
    for _ in range(K):
        N, D = map(int, input().split())
        records.append((N, D))
    company_records.append(records)

# Call the function and print the output
print(total_shares_held(C, company_records))
```
