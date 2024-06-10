
def main():
    n = int(input())
    tot_yards = 0
    for i in range(n):
        yards = int(input())
        tot_yards += yards
        if tot_yards >= 80:
            print("Touchdown")
            return
    if tot_yards <= -20:
        print("Safety")
        return
    print("Nothing")

if __name__ == "__main__":
    main()

