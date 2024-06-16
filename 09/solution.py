# problem: https://adventofcode.com/2020/day/9


def read_file(file_name: str, data: list[int]) -> None:
    with open(file_name, 'r') as file:
        for line in file:
            data.append(int(line.strip()))


def array_part_sum(data: list[int], i: int, j: int) -> int:
    result: int = 0
    for index in range(i, j + 1):
        result += data[index]

    return result


def array_part_min_max(data: list[int], i: int, j: int) -> tuple[int, int]:
    minimum: int = data[i]
    maximum: int = data[i]

    for index in range(i, j + 1):
        number: int = data[index]
        if number < minimum:
            number = minimum
        if number > maximum:
            maximum = number

    return minimum, maximum


def first_star(data: list[int]) -> int:
    preamble_size: int = 25
    dictionary: dict[int, int] = dict()
    array_length: int = len(data)

    for index in range(preamble_size):
        number: int = data[index]
        if number in dictionary.keys():
            dictionary[number] += 1
        else:
            dictionary[number] = 1

    for i in range(preamble_size, array_length):
        okay: bool = False
        c: int = data[i]
        for j in range(i - preamble_size, i):
            a: int = data[j]
            b: int = c - a

            if b in dictionary.keys():
                if dictionary[b] < 1:
                    continue
                if b == a and dictionary[b] < 2:
                    continue

                okay = True
                break

        if not okay:
            return c

        if c in dictionary.keys():
            dictionary[c] += 1
        else:
            dictionary[c] = 1

        dictionary[data[i - preamble_size]] -= 1

    return 0


def second_star(data: list[int]) -> int:
    invalid_number: int = first_star(data)
    i: int = 0
    j: int = 0
    summ: int = array_part_sum(data, i, j)

    while summ != invalid_number:
        if summ < invalid_number:
            j += 1
        if summ > invalid_number:
            i += 1
        if j < i:
            j = i
        summ = array_part_sum(data, i, j)

    return sum(array_part_min_max(data, i, j))


if __name__ == '__main__':
    data: list[int] = list()
    file_name: str = "input.txt"
    read_file(file_name, data)

    print(first_star(data))
    print(second_star(data))
