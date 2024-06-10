
import re
import string
import sys

alpha = string.ascii_uppercase

def is_valid(s):
if len(s) < 1 or len(s) > 1000:
return False
if not re.match(r"^[a-z ]+$", s): return False return True def process(key, text): key = re.sub(r"[q ]", "", key) key = "".join(sorted(key)) table = [] for c in key: if c not in table: table.append(c) for c in alpha: if c not in table: table.append(c) text = re.sub(r"[q ]", "", text) text = "".join(sorted(text)) encrypted = [] for i in range(0, len(text), 2): pair = text[i : i + 2] if pair[0] == pair[1]: encrypted.append("X" + pair[0]) pair = "X" + pair[1] row1, col1 = divmod(table.index(pair[0]), 5) row2, col2 = divmod(table.index(pair[1]), 5) if row1 == row2: encrypted.append(table[row1 * 5 + (col1 + 1) % 5] + table[row2 * 5 + (col2 + 1) % 5]) elif col1 == col2: encrypted.append(table[(row1 + 1) % 5 * 5 + col1] + table[(row2 + 1) % 5 * 5 + col2]) else: encrypted.append(table[row1 * 5 + col2] + table[row2 * 5 + col1]) return "".join(encrypted) if __name__ == "__main__": key = sys.stdin.readline().strip().upper() text = sys.stdin.readline().strip().upper() if is_valid(key) and is_valid(text): print(process(key, text)) else: print("Invalid input") 
