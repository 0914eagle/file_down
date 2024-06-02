
def is_adorable(s):
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1
    
    unique_counts = set(counts.values())
    
    if len(unique_counts) != 2:
        return "No"
    
    if abs(unique_counts.pop() - unique_counts.pop()) <= 1:
        return "Yes"
    else:
        return "No"

s = input().strip()
print(is_adorable(s))
