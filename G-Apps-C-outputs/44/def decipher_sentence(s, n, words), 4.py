
def decipher_sentence(s, n, words):
    def is_valid_word(word):
        return word in words
    
    def decipher_helper(s, start, end, memo):
        if start > end:
            return ''
        
        if (start, end) in memo:
            return memo[(start, end)]
        
        if start == end:
            return s[start]
        
        if is_valid_word(s[start:end+1]):
            return s[start:end+1]
        
        for i in range(start, end):
            left = decipher_helper(s, start, i, memo)
            right = decipher_helper(s, i+1, end, memo)
            
            if left != 'impossible' and right != 'impossible':
                return left + ' ' + right
        
        memo[(start, end)] = 'impossible'
        return 'impossible'
    
    words = set(words)
    memo = {}
    result = decipher_helper(s, 0, len(s)-1, memo)
    
    if result == 'impossible':
        return 'impossible'
    elif ' ' in result:
        return 'ambiguous'
    else:
        return result

# Input parsing
s = input().strip()
n = int(input().strip())
words = [input().strip() for _ in range(n)]

# Call the function
output = decipher_sentence(s, n, words)
print(output)
