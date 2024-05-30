
def compare(a,b):
    if a+b < b+a:
        return a+b
    else:
        return b+a

def main():
    a,b = input().split()
    a = int(a)
    b = int(b)
    print(compare(a,b))

if __name__ == '__main__':
    main()

