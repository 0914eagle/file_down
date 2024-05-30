
def compare(a, b):
    return str(b) + str(a) if a > b else str(a) + str(b)

def main():
    a, b = input().split()
    print(compare(int(a), int(b)))

