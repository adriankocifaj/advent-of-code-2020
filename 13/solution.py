# problem: https://adventofcode.com/2020/day/13


import math


def read_file(file_name: str, data: list[str]) -> int:
    with open(file_name, 'r') as file:
        number: int = int(file.readline().strip())
        for value in file.readline().strip().split(","):
            data.append(value)

    return number


def least_common_multiple(n1: int, n2: int) -> int:
    number1: int = n1
    number2: int = n2
    while number1 != number2:
        if number1 < number2:
            number1 += math.ceil((number2 - number1) / n1) * n1
        else:
            number2 += math.ceil((number1 - number2) / n2) * n2

    return number1


def first_star(data: list[str], arrival: int) -> int:
    closest_arrival: int = 2 ** 64
    bus_id: int = 0

    for i in range(len(data)):
        if data[i] == "x":
            continue

        number: int = int(data[i])
        times: int = arrival // number if arrival % number == 0 else arrival // number + 1
        bus_arrival: int = number * times
        if bus_arrival < closest_arrival:
            closest_arrival = bus_arrival
            bus_id = number

    return (closest_arrival - arrival) * bus_id


def second_star(data: list[str]) -> int:
    number1: int = int(data[0])
    n1: int = number1

    for i in range(1, len(data)):
        if data[i] == "x":
            continue

        number2: int = int(data[i])
        n2: int = number2
        while number1 != number2 - i:
            if number1 < number2 - i:
                number1 += math.ceil((number2 - i - number1) / n1) * n1
            else:
                number2 += math.ceil((number1 + i - number2) / n2) * n2

        n1 = least_common_multiple(n1, n2)

    return number1


if __name__ == '__main__':
    data: list[str] = list()
    file_name: str = "input.txt"
    arrival: int = read_file(file_name, data)

    print(first_star(data, arrival))
    print(second_star(data))
