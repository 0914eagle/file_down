
def is_adorable(s):
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    
    if len(count) < 2:
        return "No"
    
    max_count = max(count.values())
    min_count = min(count.values())
    
    if max_count >= 2 and min_count >= 1 and max_count != min_count:
        return "Yes"
    else:
        return "No"

s = input().strip()
print(is_adorable(s))
