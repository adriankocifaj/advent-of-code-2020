# problem: https://adventofcode.com/2020/day/5


def read_file(file_name: str, data: list[str]) -> None:
    with open(file_name, 'r') as file:
        for line in file:
            data.append(line.strip())


def get_seat_id(string: str) -> int:
    row: list[int] = [0, 127]
    col: list[int] = [0, 7]

    for character in string[:7]:
        if character == "F":
            row[1] = int((row[0] + row[1]) / 2)
        else:
            row[0] = int((row[0] + row[1]) / 2 + 1)

    for character in string[7:]:
        if character == "L":
            col[1] = int((col[0] + col[1]) / 2)
        else:
            col[0] = int((col[0] + col[1]) / 2 + 1)

    return row[0] * 8 + col[0]


def first_star(data: list[str]) -> int:
    highest_seat_id: int = 0

    for string in data:
        seat_id: int = get_seat_id(string)
        if seat_id > highest_seat_id:
            highest_seat_id = seat_id

    return highest_seat_id


def second_star(data: list[str]) -> int:
    highest_possible_seat_id: int = 127 * 8 + 8
    lowest_possible_seat_id: int = 0
    highest_seat_id: int = lowest_possible_seat_id
    lowest_seat_id: int = highest_possible_seat_id
    all_ids = set(number for number in range(highest_possible_seat_id + 1))

    for string in data:
        seat_id: int = get_seat_id(string)

        if seat_id < lowest_seat_id:
            lowest_seat_id = seat_id
        if seat_id > highest_seat_id:
            highest_seat_id = seat_id

        all_ids.remove(seat_id)

    for seat_id in all_ids:
        if lowest_seat_id < seat_id < highest_seat_id:
            return seat_id

    return 0


if __name__ == '__main__':
    data: list[str] = list()
    file_name: str = "input.txt"
    read_file(file_name, data)

    print(first_star(data))
    print(second_star(data))
