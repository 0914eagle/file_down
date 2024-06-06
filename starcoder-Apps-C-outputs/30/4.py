
# 去除掉字符串的空格
sentence = raw_input().replace(" ", "")
# 字典的数量
n = int(raw_input())
# 新建一个字典，然后将字典里面的单词按长度从大到小排列
d = [raw_input() for _ in xrange(n)]
d.sort(key=lambda x: -len(x))

# 如果所有的字母都可以匹配单词，就返回True
def all_matched(s):
    return not any(c not in s for c in "abcdefghijklmnopqrstuvwxyz")
# 这个函数用于判断这个单词是否存在于字符串中，若存在，则将该单词从字符串中剔除，并返回True
def is_in(s, w):
    if w in s:
        s = s.replace(w, "", 1)
        return True
    return False

# 字符串的长度
l = len(sentence)
for i in xrange(l):
    for w in d:
        if w in sentence[i:] and len(sentence[i:]) <= l/2 and all_matched(sentence[i:]):
            l = l-len(w)
            break
# 如果l<=0，就输出impossible，如果l>0，则输出ambiguous
if l <= 0:
    print "impossible"
else:
    print "ambiguous"
