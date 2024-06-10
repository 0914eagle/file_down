
def solve(table):
    n, m = len(table), len(table[0])
    rows = ["".join(row) for row in table]
    
    count = 0
    for j in range(m):
        col = [row[j] for row in table]
        if all(rows[i] <= rows[i+1] for i in range(n-1)):
            break
        
        count += 1
        
    return count
    
if __name__ == '__main__':
    n, m = map(int, input().split())
    table = [input() for _ in range(n)]
    
    print(solve(table))

