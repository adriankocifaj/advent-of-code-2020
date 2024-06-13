

# problem: https://adventofcode.com/2020/day/1


def read_file(file_name: str, values: list) -> None:
    with open(file_name, 'r') as file:
        for line in file:
            value: int = int(line.strip())
            values.append(value)


def first_star(values: list, target_value: int) -> int:
    left: int = 0
    right: int = len(values) - 1

    while left < right:
        a: int = values[left]
        b: int = values[right]
        result: int = target_value - a - b

        if result == 0:
            return a * b
        elif result < 0:
            right -= 1
        else:
            left += 1

    return 0


def second_star(values: list, target_value: int) -> int:
    array_length: int = len(values)

    for i in range(1, len(values) - 1):
        c: int = values[i]
        left: int = 0
        right: int = array_length - 1

        while left != i and right != i:
            a: int = values[left]
            b: int = values[right]
            result: int = target_value - a - b - c

            if result == 0:
                return a * b * c
            elif result < 0:
                right -= 1
            else:
                left += 1

    return 0


if __name__ == '__main__':
    values: list = list()
    file_name: str = "input.txt"
    read_file(file_name, values)
    values.sort()
    target_value: int = 2020

    print(first_star(values, target_value))
    print(second_star(values, target_value))
