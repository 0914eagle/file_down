
def get_abc_abbreviation(n):
    return "ABC" + str(n).rjust(3, "0")

if __name__ == "__main__":
    n = int(input())
    print(get_abc_abbreviation(n))

