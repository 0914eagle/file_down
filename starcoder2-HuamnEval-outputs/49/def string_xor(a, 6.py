
 def string_xor(a: str, b: str) -> str:
    
    result = []
    for i, j in zip(a, b):
        result.append(str(int(i) ^ int(j)))
    return ''.join(result)
