
#!/usr/bin/env python

import re
import sys

class Rebus(object):
    def __init__(self, string):
        self.string = string
        self.num_regex = re.compile(r"\d+")
        self.parts = string.split(" ")

    def get_numbers(self):
        return [int(num) for num in self.num_regex.findall(self.string)]

    def get_operators(self):
        return [part for part in self.parts if part not in self.get_numbers()]

    def get_total(self):
        return self.get_numbers()[-1]

    def solve(self):
        numbers = self.get_numbers()
        operators = self.get_operators()
        total = self.get_total()
        for num1 in range(1, total+1):
            for num2 in range(1, total+1):
                for num3 in range(1, total+1):
                    for num4 in range(1, total+1):
                        for num5 in range(1, total+1):
                            equation = "{} {} {} {} {} {} {} {}".format(
                                num1, operators[0], num2, operators[1], num3,
                                operators[2], num4, total
                            )
                            if eval(equation):
                                return equation

        return "Impossible"

if __name__ == "__main__":
    rebus = Rebus(sys.stdin.read().strip())
    print(rebus.solve())

