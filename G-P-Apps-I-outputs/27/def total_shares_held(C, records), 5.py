
def total_shares_held(C, records):
    daily_totals = {}
    
    for company_records in records:
        for shares, day in company_records:
            if day not in daily_totals:
                daily_totals[day] = shares
            else:
                daily_totals[day] += shares
                
    output = [daily_totals[day] for day in sorted(daily_totals.keys())]
    return ' '.join(map(str, output))

# Input parsing
C = int(input())
records = []
for _ in range(C):
    company_records = []
    K = int(input())
    for _ in range(K):
        N, D = map(int, input().split())
        company_records.append((N, D))
    records.append(company_records)

# Call the function and print the output
print(total_shares_held(C, records))
```
