
# 1. 题目大意
# 给定一个n*n的矩阵，要求将其分解为两个n*n的矩阵，其中一个矩阵是对称的，另一个矩阵是反对称的，且两者之和等于原矩阵

# 2. 解题思路
# 首先，对称矩阵和反对称矩阵的定义：
# 对称矩阵：A_{ij} = A_{ji}
# 反对称矩阵：A_{ij} = -A_{ji}
# 因此，可以得到：
# A_{ij} = A_{ji} = 1/2*(W_{ij} + W_{ji})
# A_{ij} = -A_{ji} = 1/2*(W_{ij} - W_{ji})
# 因此，可以得到：
# A_{ij} = 1/2*(W_{ij} + W_{ji})
# B_{ij} = 1/2*(W_{ij} - W_{ji})
# 因此，可以得到：
# A_{ij} + B_{ij} = W_{ij}

# 3. 代码
