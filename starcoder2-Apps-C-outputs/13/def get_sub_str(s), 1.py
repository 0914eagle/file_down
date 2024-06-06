
def get_sub_str(s):
    ans = 0
    for i in range(len(s)):
        for j in range(i,len(s)):
            if s[i:j+1] == s[i:j+1][::-1]:
                ans += 1
    return ans
