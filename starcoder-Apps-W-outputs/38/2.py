
# Author : 
# Date   : 22 August, 2020

def main():
    a = input()
    b = input()
    if len(a) != len(b):
        print("NO")
        exit(0)
    for i in range(len(a)):
        if a[i] == '1' and b[i] == '0':
            print("NO")
            exit(0)
    print("YES")


if __name__ == "__main__":
    main()

