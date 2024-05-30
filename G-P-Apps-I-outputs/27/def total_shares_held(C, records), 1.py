
def total_shares_held(C, records):
    all_days = set()
    for company_records in records:
        for shares, day in company_records:
            all_days.add(day)

    all_days = sorted(list(all_days))
    total_shares = [0] * len(all_days)

    for company_records in records:
        for shares, day in company_records:
            idx = all_days.index(day)
            total_shares[idx] += shares

    return total_shares

# Input processing
C = int(input())
records = []

for _ in range(C):
    K = int(input())
    company_records = []
    for _ in range(K):
        N, D = map(int, input().split())
        company_records.append((N, D))
    records.append(company_records)

# Calculate total shares held for each day
result = total_shares_held(C, records)

# Output the result
print(" ".join(map(str, result)))
```

Feel free to test this code with the sample input provided. Let me know if you need any further assistance! 
