
def main():
    # Please add your code here
    n, p = map(float, input().split())
    boxes = []
    for i in range(int(n)):
        energy, prob = map(float, input().split())
        boxes.append((energy, prob))
    boxes.sort(key=lambda x: x[0] * x[1])
    psum = 0
    for energy, prob in boxes:
        if psum + prob >= p:
            print(energy)
            return
    print(0)

if __name__ == '__main__':
    main()
