
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

def round_up(num, divisor):
    return num + (divisor - num % divisor)

def order(time, dish):
    if dish == "ABC Don":
        time = round_up(time, 10)
        time += A
    elif dish == "ARC Curry":
        time = round_up(time, 10)
        time += B
    elif dish == "AGC Pasta":
        time = round_up(time, 10)
        time += C
    elif dish == "ATC Hanbagu":
        time = round_up(time, 10)
        time += D
    elif dish == "APC Ramen":
        time = round_up(time, 10)
        time += E
    return time

time = 0
time = order(time, "ABC Don")
time = order(time, "ARC Curry")
time = order(time, "AGC Pasta")
time = order(time, "ATC Hanbagu")
time = order(time, "APC Ramen")

print(time)

