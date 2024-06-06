
import sys

# 从输入流读取数据
def read_input():
    line = sys.stdin.readline().rstrip()
    return line

# 输出数据到输出流
def write_output(result):
    print(result)

# 计算最终结果
def process_data(sentence, dictionary):
    # 记录所有的可能解，可能有多个
    possible_solutions = []
    # 对所有可能的分割方式进行深度优先遍历，找到所有可能的解
    # 从第一个位置开始，尝试用所有的词语对它进行替换
    for word in dictionary:
        # 如果该词语可以和原字符串的第一个位置匹配
        if sentence[:len(word)] == word:
            # 如果当前字符串长度比词语长度短，说明该词语就是它了
            if len(sentence) == len(word):
                possible_solutions.append([word])
            # 否则继续用深度优先遍历的方式，寻找下一个词语
            else:
                # 把当前词语替换之后的剩余字符串作为子问题，递归调用
                next_solutions = process_data(sentence[len(word):], dictionary)
                for solution in next_solutions:
                    solution.insert(0, word)
                    possible_solutions.append(solution)
    # 最终只返回所有可能解中的第一个
    if len(possible_solutions) == 0:
        return ['impossible']
    elif len(possible_solutions) > 1:
        return ['ambiguous']
    else:
        return ' '.join(possible_solutions[0])

# 主函数
def main():
    sentence = read_input()
    n = int(read_input())
    dictionary = []
    for _ in range(n):
        dictionary.append(read_input())
    result = process_data(sentence, dictionary)
    write_output(result)

# 主函数调用
if __name__ == '__main__':
    main()

