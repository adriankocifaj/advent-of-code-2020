# problem: https://adventofcode.com/2020/day/10


def read_file(file_name: str, data: list[int]) -> None:
    with open(file_name, 'r') as file:
        for line in file:
            data.append(int(line.strip()))


def first_star(data: list[int]) -> int:
    jolts: list[int] = [0, 0, 0]
    array_length: int = len(data)

    for index in range(0, array_length - 1):
        number1: int = data[index]
        number2: int = data[index + 1]
        jolts[number2 - number1 - 1] += 1

    return jolts[0] * (jolts[2] + 1)


def second_star(data: list[int]) -> int:
    array_length: int = len(data)
    ways: list[int] = [0] * array_length
    ways[0] = 1

    for i in range(array_length):
        for j in range(3):
            if i + j + 1 >= array_length:
                continue
            if data[i + j + 1] - data[i] <= 3:
                ways[i + j + 1] += ways[i]

    return ways[-1]


if __name__ == '__main__':
    data: list[int] = [0]
    file_name = "input.txt"
    read_file(file_name, data)
    data.sort()

    print(first_star(data))
    print(second_star(data))
