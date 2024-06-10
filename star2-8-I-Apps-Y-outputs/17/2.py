
import sys

def is_satisfactory(m, n, clauses):
    if m < 8:
        return "unsatisfactory"
    else:
        return "satisfactory"

def main():
    m, n = map(int, sys.stdin.readline().split())
    clauses = []
    for _ in range(m):
        clause = list(map(int, sys.stdin.readline().split()))
        assert len(clause) == 3
        clauses.append(clause)
    print(is_satisfactory(m, n, clauses))

if __name__ == "__main__":
    main()

