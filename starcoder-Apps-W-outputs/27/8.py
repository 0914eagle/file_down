
##python
n = int(input())
ans = [''] * 26
li = []
for _ in range(n):
    li.append(input())
li.sort()
## 前一个字母要比后一个字母小
## 所以相同前缀的字母是一定要连续的
## 这里就相当于贪心 
for i in range(n - 1):
    for j in range(min(len(li[i]),len(li[i+1]))):
        if li[i][j] != li[i+1][j]:
            break
    else:
        continue
    if ans[ord(li[i][j]) - ord('a')] == '':
        ans[ord(li[i][j]) - ord('a')] = li[i+1][j]
    else:
        ans[ord(li[i+1][j]) - ord('a')] = li[i][j]
## 只有从前往后 才能保证顺序
## 若不连续 则必定会有一段区间出现多次
## 所以 相同前缀的字母一定是连续的
## 所以 相当于对一个有序序列 贪心
for i in range(len(li[n-1])):
    if ans[ord(li[n-1][i]) - ord('a')] == '':
        ans[ord(li[n-1][i]) - ord('a')] = li[n-1][i]
    else:
        if ans[ord(li[n-1][i]) - ord('a')] != li[n-1][i]:
            print('Impossible')
            exit()
res = ''
for i in ans:
    if i == '':
        continue
    res += i
print(res)
