# problem: https://adventofcode.com/2020/day/7


def read_file(file_name: str, data: dict[str, dict[str, int]]) -> None:
    with open(file_name, 'r') as file:
        for line in file:
            bag, items = line.strip().split(" bags contain ")
            data[bag] = dict()
            for item in items.split(", "):
                values: list[str] = item.split(" ")
                if values[0] != "no":
                    data[bag][values[1] + " " + values[2]] = int(values[0])


def contains_shiny_gold_bag(bag: str, data: dict[str, dict[str, int]]) -> bool:
    for item in data[bag]:
        if item == "shiny gold" or contains_shiny_gold_bag(item, data):
            return True

    return False


def bag_counter(bag: str, data: dict[str, dict[str, int]]) -> int:
    counter: int = 0

    for item in data[bag]:
        counter += data[bag][item] + data[bag][item] * bag_counter(item, data)

    return counter


def first_star(data: dict[str, dict[str, int]]) -> int:
    counter: int = 0

    for bag in data:
        if contains_shiny_gold_bag(bag, data):
            counter += 1

    return counter


def second_star(data: dict[str, dict[str, int]]) -> int:
    return bag_counter("shiny gold", data)


if __name__ == '__main__':
    data: dict[str, dict[str, int]] = dict()
    file_name: str = "input.txt"
    read_file(file_name, data)

    print(first_star(data))
    print(second_star(data))
