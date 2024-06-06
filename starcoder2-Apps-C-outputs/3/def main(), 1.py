
def main():
    s = input()
    n = int(input())
    words = [input() for _ in range(n)]
    words.sort(key=lambda x: len(x), reverse=True)
    res = []
    for word in words:
        if s.find(word) != -1:
            res.append(word)
            s = s.replace(word, '')
    if len(s) == 0:
        print(' '.join(res))
    else:
        print('impossible')

if __name__ == '__main__':
    main()
