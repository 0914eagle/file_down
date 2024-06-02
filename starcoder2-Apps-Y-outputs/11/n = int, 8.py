
n = int(input())
s = input()

two_gram = ""
max_count = 0

for i in range(n-1):
    gram = s[i:i+2]
    count = s.count(gram)
    if count > max_count:
        two_gram = gram
        max_count = count

print(two_gram)

