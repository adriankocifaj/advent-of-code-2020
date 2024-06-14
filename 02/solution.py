

# problem: https://adventofcode.com/2020/day/2


def read_file(file_name: str, data: list) -> None:
    with open(file_name, 'r') as file:
        for line in file:
            parts: list = line.strip().split(" ")
            numbers: list = parts[0].split("-")

            minimum: int = int(numbers[0])
            maximum: int = int(numbers[1])
            character: str = parts[1][:len(parts) - 2]
            string: str = parts[2]
            data.append(tuple((minimum, maximum, character, string)))


def first_star(data: list) -> int:
    valid: int = 0

    for minimum, maximum, character, string in data:
        counter: int = string.count(character)

        if minimum <= counter <= maximum:
            valid += 1

    return valid


def second_star(data: list) -> int:
    valid: int = 0

    for i, j, character, string in data:
        if int(character == string[i - 1]) ^ int(character == string[j - 1]):
            valid += 1

    return valid


if __name__ == '__main__':
    data: list = list()
    file_name: str = "input.txt"
    read_file(file_name, data)

    print(first_star(data))
    print(second_star(data))
