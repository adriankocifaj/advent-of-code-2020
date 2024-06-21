# problem: https://adventofcode.com/2020/day/18


class Equation:
    def __init__(self, string: str) -> None:
        self.values: list[int | str | Equation] = list()

        index: int = 0
        current: str = ""
        while index < len(string):
            character: str = string[index]
            if character == "+" or character == "*":
                self.values.append(character)
            elif character == " ":
                if len(current):
                    self.values.append(int(current))
                    current = ""
            elif "0" <= character <= "9":
                current += character
            elif character == "(":
                counter: int = 1
                index += 1
                while counter:
                    character = string[index]
                    if character == "(":
                        counter += 1
                    if character == ")":
                        counter -= 1
                    if counter:
                        current += character
                        index += 1
                self.values.append(Equation(current))
                current = ""

            index += 1

        if len(current):
            self.values.append(int(current))

    def evaluate(self, plus_first: bool) -> int:
        if plus_first:
            for index in range(len(self.values)):
                if self.values[index] == "+":
                    left: int | Equation = self.values[index - 1]
                    right: int | Equation = self.values[index + 1]
                    e1: Equation = Equation("")
                    e2: Equation = Equation("")
                    e1.values = [left]
                    e2.values = [right]
                    self.values[index - 1] = 1
                    self.values[index] = "*"
                    self.values[index + 1] = e1.evaluate(plus_first) + e2.evaluate(plus_first)

        result: int = 0
        operation: int = 0
        for value in self.values:
            if isinstance(value, int):
                if not operation:
                    result += value
                else:
                    result *= value

            elif isinstance(value, Equation):
                if not operation:
                    result += value.evaluate(plus_first)
                else:
                    result *= value.evaluate(plus_first)

            else:
                if value == "+":
                    operation = 0
                else:
                    operation = 1

        return result


def read_file(file_name: str, equations: list[Equation]) -> None:
    with open(file_name, 'r') as file:
        for line in file:
            equations.append(Equation(line.strip()))


def solution(equations: list[Equation], plus_first: bool) -> int:
    return sum(equation.evaluate(plus_first) for equation in equations)


if __name__ == '__main__':
    equations: list[Equation] = list()
    file_name: str = "input.txt"
    read_file(file_name, equations)

    print(solution(equations, False))
    print(solution(equations, True))
