# problem: https://adventofcode.com/2020/day/8


def read_file(file_name: str, data: list[tuple[str, int]]) -> None:
    with open(file_name) as file:
        for line in file:
            instruction, value = line.strip().split(" ")
            data.append((instruction, int(value)))


def first_star(data: list[tuple[str, int]]) -> int:
    accumulator: int = 0
    visited: set[int] = set()
    index: int = 0

    while index not in visited:
        visited.add(index)
        instruction, value = data[index]

        if instruction == "nop":
            index += 1
        elif instruction == "acc":
            accumulator += value
            index += 1
        else:
            index += value

    return accumulator


def second_star(data: list[tuple[str, int]]) -> int:
    accumulator: int = 0
    visited: set[int] = set()
    instruction_order: list[int] = list()
    index: int = 0
    array_length: int = len(data)

    # first run program to know what instructions affect the loop
    while index not in visited:
        visited.add(index)
        instruction_order.append(index)
        instruction, value = data[index]

        if instruction == "nop":
            index += 1
        elif instruction == "acc":
            index += 1
        else:
            index += value

    # change instruction one at a time and run the program to find the one that terminates
    for instruction_index in instruction_order:
        instruction, value = data[instruction_index]
        if instruction == "acc":
            continue
        elif instruction == "nop":
            data[instruction_index] = ("jmp", value)
        else:
            data[instruction_index] = ("nop", value)

        visited.clear()
        accumulator = 0
        index = 0

        while index not in visited:
            if index < 0:
                break

            if index == array_length:
                return accumulator

            visited.add(index)
            i, v = data[index]

            if i == "nop":
                index += 1
            elif i == "acc":
                accumulator += v
                index += 1
            else:
                index += v

        if instruction == "nop":
            data[instruction_index] = ("nop", value)
        else:
            data[instruction_index] = ("jmp", value)

    return accumulator


if __name__ == '__main__':
    data: list[tuple[str, int]] = list()
    file_name: str = "input.txt"
    read_file(file_name, data)

    print(first_star(data))
    print(second_star(data))
