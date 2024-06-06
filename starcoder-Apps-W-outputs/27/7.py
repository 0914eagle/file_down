
# 解题思路

# 我们可以这样想，对于两位作者的名字，如果他们的名字首字母不同，那么首字母小的一定在前面；如果首字母相同，那么我们需要比较下一位，以此类推。
# 这样我们可以知道，作者名字的字母顺序和作者名字的首字母字母顺序是一致的。

# 所以我们只需要对作者名字的首字母进行排序，如果首字母相同，我们再比较下一位，直到我们比较出大小为止。
# 这样我们就可以知道，如果排序完的顺序和原来的首字母顺序一致，那么作者名字的顺序是按照字典顺序排列的。
# 因此我们对作者名字的首字母排序，如果和原来不一致，那么我们就输出“Impossible”；否则，我们输出排序后的首字母顺序。


# 作者名字
names = [""] * int(input())

# 首字母顺序
first_letter = [""] * int(input())

# 首字母顺序是否和排序后的首字母顺序一致
is_sorted = True

for i in range(int(input())):
    names[i] = input()
    first_letter[i] = names[i][0]

# 首字母排序
first_letter.sort()

# 首字母排序
for i in range(len(first_letter)):
    if first_letter[i] != names[i][0]:
        is_sorted = False

# 如果首字母顺序和排序后的首字母顺序一致，那么作者名字的顺序是按照字典顺序排列的。
if is_sorted:
    print("".join(first_letter))
else:
    print("Impossible")
