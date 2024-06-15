# problem: https://adventofcode.com/2020/day/6


def read_file(file_name: str, data: list[dict[str, int]], people_counter: list[int]) -> None:
    with open(file_name, 'r') as file:
        data.append(dict())
        people_counter.append(0)
        for line in file:
            if line.strip() == "":
                data.append(dict())
                people_counter.append(0)
                continue
            for character in line.strip():
                if character in data[-1].keys():
                    data[-1][character] += 1
                    continue
                data[-1][character] = 1
            people_counter[-1] += 1


def first_star(data: list[dict[str, int]]) -> int:
    counter: int = 0

    for group in data:
        counter += len(group)

    return counter


def second_star(data: list[dict[str, int]], people_counter: list[int]) -> int:
    counter: int = 0
    index: int = 0

    for group in data:
        for question in group:
            if group[question] == people_counter[index]:
                counter += 1
        index += 1

    return counter


if __name__ == '__main__':
    data: list[dict[str, int]] = list()
    people_counter: list[int] = list()
    file_name: str = "input.txt"
    read_file(file_name, data, people_counter)

    print(first_star(data))
    print(second_star(data, people_counter))
