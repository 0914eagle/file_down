

def solve(table):
    n = len(table)
    m = len(table[0])
    
    def is_good(table, removed):
        rows = ["".join(c for i, c in enumerate(row) if i not in removed) for row in table]
        return sorted(rows) == rows
    
    def count_good_cols(table):
        count = 0
        for j in range(m):
            if is_good(table, {j}):
                count += 1
        return count
    
    return m - count_good_cols(table)
    
if __name__ == "__main__":
    n, m = map(int, input().split())
    table = [input() for _ in range(n)]
    
    print(solve(table))
    

