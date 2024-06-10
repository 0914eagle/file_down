
nm = list(map(int,input().split()))
min_ = min(nm)
max_ = max(nm)
if max_ < 3:
    print(0)
elif max_ == 3:
    print(1)
else:
    print(min_ * 2 + 1)

