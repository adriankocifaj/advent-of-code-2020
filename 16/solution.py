# problem: https://adventofcode.com/2020/day/16


def read_file(file_name: str, data: dict[str, set[int]], nearby_tickets: list[list[int]]) -> list[int]:
    my_ticket: list[int] = list()
    stage: int = 0
    with open(file_name, 'r') as file:
        for line in file:
            if line.strip() == "":
                continue
            if line.strip() in ["your ticket:", "nearby tickets:"]:
                stage += 1
                continue

            match stage:
                case 0:
                    field, ranges = line.strip().split(": ")
                    data[field] = set()
                    ranges = ranges.split(" or ")
                    for value in ranges:
                        left, right = [int(number) for number in value.split("-")]
                        for number in range(left, right + 1):
                            data[field].add(number)

                case 1:
                    my_ticket = [int(number) for number in line.strip().split(",")]

                case 2:
                    nearby_tickets.append([int(number) for number in line.strip().split(",")])

    return my_ticket


def first_star(data: dict[str, set[int]], nearby_tickets: list[list[int]]) -> int:
    result: int = 0

    for ticket in nearby_tickets:
        for number in ticket:
            okay: bool = False
            for field in data:
                if number in data[field]:
                    okay = True
                    break
            if not okay:
                result += number

    return result


def second_star(data: dict[str, set[int]], nearby_tickets: list[list[int]], my_ticket: list[int]) -> int:
    # filter out invalid tickets
    valid_tickets: list[list[int]] = list()
    for ticket in nearby_tickets:
        valid: bool = True
        for number in ticket:
            okay: bool = False
            for field in data:
                if number in data[field]:
                    okay = True
                    break
            if not okay:
                valid = False
                break
        if valid:
            valid_tickets.append(ticket)

    # arrange fields
    fields: dict[str, set[int]] = dict()
    for field in data.keys():
        fields[field] = set()
        for i in range(len(my_ticket)):
            okay: bool = True
            for ticket in valid_tickets:
                if ticket[i] not in data[field]:
                    okay = False
                    break
            if okay:
                fields[field].add(i)

    arranged_fields: list[str] = [""] * len(data)
    arranged: set[int] = set()
    for i in range(len(data)):
        for field in fields:
            values: list[int] = list(fields[field] - arranged)
            if len(values) == 1:
                arranged_fields[values[0]] = field
                arranged.add(values[0])
                fields.pop(field)
                break

    # get result
    result: int = 0
    for index in range(len(arranged_fields)):
        if "departure" in arranged_fields[index]:
            if result == 0:
                result = 1
            result *= my_ticket[index]

    return result


if __name__ == '__main__':
    data: dict[str, set[int]] = dict()
    nearby_tickets: list[list[int]] = list()
    file_name: str = "input.txt"
    my_ticket: list[int] = read_file(file_name, data, nearby_tickets)

    print(first_star(data, nearby_tickets))
    print(second_star(data, nearby_tickets, my_ticket))
