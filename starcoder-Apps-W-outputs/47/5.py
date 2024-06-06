
# 设二维数组lst = [[a1, b1], [a2, b2], ..., [an, bm]]
# 先将lst的元素按每行第二个元素从小到大排序
lst.sort(key=lambda x: x[1])
# 再将lst的元素按每行第一个元素从大到小排序
lst.sort(key=lambda x: x[0], reverse=True)
print(lst[0][0] * lst[0][1])
