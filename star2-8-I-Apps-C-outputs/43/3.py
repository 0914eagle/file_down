
def longest_alternating_subsequence(string):
    length = len(string)
    alternating_subsequences = []
    for i in range(length):
        for j in range(i, length):
            substring = string[i:j + 1]
            alternating = True
            for k in range(1, len(substring)):
                if substring[k] == substring[k - 1]:
                    alternating = False
                    break
            if alternating:
                alternating_subsequences.append(substring)
    longest_length = 0
    for subsequence in alternating_subsequences:
        longest_length = max(longest_length, len(subsequence))

    return longest_length

def main():
    n = int(input())
    string = input()
    result = longest_alternating_subsequence(string)
    print(result)

if __name__ == "__main__":
    main()

