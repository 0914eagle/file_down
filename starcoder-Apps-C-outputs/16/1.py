
#input: number of friends and ious
#output: who owes how much
#sort all the people with IOUs
#then go through a list of ious and record who owes who how much
#remove the one with the smallest amount

num_friends, num_ious = map(int, input().split())
ious = []
for i in range(num_ious):
    a, b, c = map(int, input().split())
    ious.append((a, b, c))
ious = sorted(ious)

total_iou = [0 for i in range(num_friends)]

for i in range(num_ious):
    a, b, c = ious[i]
    total_iou[a] -= c
    total_iou[b] += c

iou_array = []
for i in range(num_friends):
    if total_iou[i] != 0:
        iou_array.append((i, total_iou[i]))

print(len(iou_array))
for i in range(len(iou_array)):
    a, b = iou_array[i]
    print(a, b)
