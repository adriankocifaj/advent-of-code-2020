# problem: https://adventofcode.com/2020/day/1


def read_file(file_name: str, data: list[int]) -> None:
    with open(file_name, 'r') as file:
        for line in file:
            value: int = int(line.strip())
            data.append(value)


def first_star(data: list[int], target_value: int) -> int:
    left: int = 0
    right: int = len(data) - 1

    while left < right:
        a: int = data[left]
        b: int = data[right]
        result: int = target_value - a - b

        if result == 0:
            return a * b
        elif result < 0:
            right -= 1
        else:
            left += 1

    return 0


def second_star(data: list[int], target_value: int) -> int:
    array_length: int = len(data)

    for i in range(1, len(data) - 1):
        c: int = data[i]
        left: int = 0
        right: int = array_length - 1

        while left != i and right != i:
            a: int = data[left]
            b: int = data[right]
            result: int = target_value - a - b - c

            if result == 0:
                return a * b * c
            elif result < 0:
                right -= 1
            else:
                left += 1

    return 0


if __name__ == '__main__':
    data: list[int] = list()
    file_name: str = "input.txt"
    read_file(file_name, data)
    data.sort()
    target_value: int = 2020

    print(first_star(data, target_value))
    print(second_star(data, target_value))
