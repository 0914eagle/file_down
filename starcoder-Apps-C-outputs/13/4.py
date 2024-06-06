
# 考虑到只有26个字母，所以可以直接暴力搜索
# 注意先把字符串转换为小写
# 然后先考虑出现的单词，并且利用单词，可以推出每个字母代表的数字
# 然后再根据单词进行逐个字母的计算

def findMax(max1, max2):
    if max1[1] > max2[1]:
        return max1
    else:
        return max2

def solve(content, knownWords):
    words = content.split()
    result = ''
    # 先考虑单词
    knownWords.sort()
    for word in knownWords:
        if word not in content:
            return 'Impossible'
    for word in knownWords:
        index = content.find(word)
        # 若单词在内容中出现，则计算
        if index != -1:
            for i in range(len(word)):
                result += chr(ord('a') + index + i)
    # 计算结果的长度
    length = len(result)
    # 然后考虑单词没有出现的，将单词逐个字母计算
    for i in range(len(words)):
        if words[i] not in knownWords:
            for j in range(len(words[i])):
                result += chr(ord('a') + (i * len(words[i]) + j) % length)
    # 因为有可能是不连续的，所以还需要计算单词出现的最大索引
    # 这里是为了把中间空的字母补上
    # 因为是按字母的索引排的
    maxIndex = 0
    for word in knownWords:
        index = content.find(word)
        if index > maxIndex:
            maxIndex = index
    # 再把单词出现的空白都补上
    for i in range(maxIndex):
        if chr(ord('a') + i) not in result:
            result += chr(ord('a') + i)
    return result

content = input()
words = ['be', 'our', 'rum', 'will', 'dead', 'hook', 'ship', 'blood', 'sable', 'avenge', 'parrot', 'captain']
print(solve(content, words))
