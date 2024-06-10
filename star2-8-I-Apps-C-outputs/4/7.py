
def mix(people, A, B, C):
    
    A, B, C = sorted([A, B, C])
    people = sorted(people, key=lambda x: (x[0], x[1], x[2]))
    count = 0
    for i in range(len(people)):
        a, b, c = people[i]
        if a >= A and b >= B and c >= C:
            count += 1
    return count

def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        people = [list(map(int, input().split())) for _ in range(N)]
        A, B, C = map(int, input().split())
        count = mix(people, A, B, C)
        print(f"Case #{i + 1}: {count}")

if __name__ == "__main__":
    main()

