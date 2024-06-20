# problem: https://adventofcode.com/2020/day/15


def read_file(file_name: str, data: list[int]) -> None:
    with open(file_name, 'r') as file:
        for number in file.readline().strip().split(","):
            data.append(int(number))


def solution(data: list[int], position: int) -> int:
    spoken: set[int] = set(data)
    numbers: dict[int, int] = dict()
    for index in range(len(data)):
        numbers[data[index]] = index

    last_number: int = 0
    for index in range(len(data), position - 1):
        if last_number not in spoken:
            numbers[last_number] = index
            spoken.add(last_number)
            last_number = 0
            continue

        last_index: int = index - numbers[last_number]
        numbers[last_number] = index
        last_number = last_index

    return last_number


if __name__ == '__main__':
    data: list[int] = list()
    file_name: str = "input.txt"
    read_file(file_name, data)

    print(solution(data, 2020))
    print(solution(data, 30000000))
