
def is_valid(num):
    s = str(num)
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                return False
    return True

def get_valid_list(num):
    valid_list = []
    for i in range(1, num):
        if is_valid(i) and is_valid(num-i) and i < num-i:
            valid_list.append((i, num-i))
    return valid_list

def main():
    num = int(input())
    valid_list = get_valid_list(num)
    print(len(valid_list))
    for i in range(min(len(valid_list), 5000)):
        print(valid_list[i][0], valid_list[i][1])

main()
