# problem: https://adventofcode.com/2020/day/14


def read_file(file_name: str, data: list[dict[int, int] | tuple[int, int]]) -> None:
    with open(file_name, 'r') as file:
        index: int = 0
        for line in file:
            instruction, value = line.strip().split(" = ")
            if instruction == "mask":
                data.append(dict())
                length: int = len(value)
                for i in range(length):
                    character: str = value[length - 1 - i]
                    if character != "X":
                        data[-1][i] = int(character)
            else:
                address: int = int(instruction.split("[")[1][:-1])
                data.append((address, int(value)))

            index += 1


def change_bit(number: int, bit_value: int, bit_index: int) -> int:
    if bit_value == 1:
        number |= 1 << bit_index
        return number

    number &= ~(1 << bit_index)
    return number


def first_star(data: list[dict[int, int] | tuple[int, int]], memory: dict[int, int]) -> int:
    current_mask: dict[int, int] = dict()

    for item in data:
        if isinstance(item, dict):
            current_mask = item
            continue

        address, value = item
        for bit_index, bit_value in current_mask.items():
            value = change_bit(value, bit_value, bit_index)

        memory[address] = value

    return sum(memory.values())


def second_star(data: list[dict[int, int] | tuple[int, int]], memory: dict[int, int]) -> int:
    current_mask: dict[int, int] = dict()
    all_addresses: set[int] = set(range(36))

    for item in data:
        if isinstance(item, dict):
            current_mask = item
            continue

        address, value = item
        for bit_index, bit_value in current_mask.items():
            if bit_value == 1:
                address = change_bit(address, bit_value, bit_index)

        floating: list[int] = list(all_addresses - set(current_mask.keys()))
        floating.sort()
        floating_length: int = len(floating)

        for number in range(2 ** floating_length):
            bits: list[int] = [(number >> i) & 1 for i in range(floating_length)]
            new_address: int = address
            for i in range(floating_length):
                new_address = change_bit(new_address, bits[i], floating[i])

            memory[new_address] = value

    return sum(memory.values())


if __name__ == '__main__':
    data: list[dict[int, int] | tuple[int, int]] = list()
    memory: dict[int, int] = dict()
    file_name: str = "input.txt"
    read_file(file_name, data)

    print(first_star(data, memory))
    memory.clear()
    print(second_star(data, memory))
