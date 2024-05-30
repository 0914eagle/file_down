
def total_shares_held(C, company_records):
    day_shares = {}
    for records in company_records:
        for record in records:
            N, D = record
            if D in day_shares:
                day_shares[D] += N
            else:
                day_shares[D] = N

    sorted_days = sorted(day_shares.keys())
    result = [day_shares[d] for d in sorted_days]
    return result

# Input processing
C = int(input())
company_records = []
for _ in range(C):
    K = int(input())
    records = []
    for _ in range(K):
        N, D = map(int, input().split())
        records.append((N, D))
    company_records.append(records)

# Call the function with input data
output = total_shares_held(C, company_records)

# Output the result
print(*output)
```
