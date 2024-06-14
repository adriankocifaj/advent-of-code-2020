# problem: https://adventofcode.com/2020/day/4


def read_file(file_name: str, data: list[dict[str, str]]) -> None:
    with open(file_name, 'r') as file:
        data.append(dict())
        index: int = 0
        for line in file:
            if line.strip() == "":
                data.append(dict())
                index += 1
                continue

            values: list[str] = line.strip().split(" ")
            for string in values:
                key, value = string.split(":")
                data[index][key] = value


def is_valid(key: str, value: str) -> bool:
    try:
        match key:
            case "byr":
                return 1920 <= int(value) <= 2002

            case "iyr":
                return 2010 <= int(value) <= 2020

            case "eyr":
                return 2020 <= int(value) <= 2030

            case "hgt":
                number: int = int(value[:-2])
                string: str = value[-2:]

                if ((string == "cm" and 150 <= number <= 193) or
                        (string == "in" and 59 <= number <= 76)):
                    return True

                return False

            case "hcl":
                if value[0] != "#" or len(value) - 1 != 6:
                    return False

                number: str = value[1:]
                for character in number:
                    if not ('a' <= character <= 'f' or '0' <= character <= '9'):
                        return False

                return True

            case "ecl":
                return value in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

            case "pid":
                int(value)
                return len(value) == 9

    except (TypeError, IndexError, ValueError):
        return False

    return True


def first_star(data: list[dict[str, str]], fields: list[str], optional: set[str]) -> int:
    counter: int = 0

    for passport in data:
        okay: bool = True
        for field in fields:
            if field in optional:
                continue
            if field not in passport.keys():
                okay = False
                break
        if okay:
            counter += 1

    return counter


def second_star(data: list[dict[str, str]], fields: list[str], optional: set[str]) -> int:
    counter: int = 0

    for passport in data:
        okay: bool = True
        for field in fields:
            if field in optional:
                continue
            if field not in passport.keys() or not is_valid(field, passport[field]):
                okay = False
                break
        if okay:
            counter += 1

    return counter


if __name__ == '__main__':
    data: list[dict[str, str]] = list()
    file_name: str = "input.txt"
    read_file(file_name, data)
    fields: list[str] = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
    optional: set[str] = {"cid"}

    print(first_star(data, fields, optional))
    print(second_star(data, fields, optional))
