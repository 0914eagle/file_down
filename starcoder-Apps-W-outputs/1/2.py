

def getInput(filename):
    import os
    dir = os.path.dirname(__file__)
    with open(dir+"\\"+filename) as file:
        lines = file.readlines()
    return lines

def makePairs(lines):
    lines = lines.strip().split(' ')
    lines = [int(line) for line in lines]
    n = lines[0]
    m = lines[1]
    lines = lines[2:]
    out = []
    for i in range(m):
        out.append((lines[i*2],lines[i*2+1]))
    return out

def rotationallySymmetrical(n,m):
    pairs = makePairs(m)
    for i in range(n):
        ans = True
        for pair in pairs:
            if pair[0] == pair[1]:
                continue
            if pair[0] + i == pair[1] or pair[1] + i == pair[0]:
                ans = True
            else:
                ans = False
                break
        if ans == True:
            return "Yes"
    return "No"

def main():
    lines = getInput("1405a.in")
    n = lines[0]
    m = lines[1]
    print(rotationallySymmetrical(n,m))

if __name__ == "__main__":
    main()

