# problem: https://adventofcode.com/2020/day/12


def read_file(file_name: str, data: list[tuple[str, int]]) -> None:
    with open(file_name, 'r') as file:
        for line in file:
            information: str = line.strip()
            data.append((information[0], int(information[1:])))


def first_star(data: list[tuple[str, int]]) -> int:
    position: list[int] = [0, 0]
    direction: int = 0

    for instruction, value in data:
        match instruction:
            case "N":
                position[0] += value
            case "S":
                position[0] -= value
            case "E":
                position[1] += value
            case "W":
                position[1] -= value
            case "R":
                direction += value
                direction %= 360
            case "L":
                direction -= value
                direction %= 360
            case "F":
                match direction:
                    case 0:
                        position[1] += value
                    case 90:
                        position[0] -= value
                    case 180:
                        position[1] -= value
                    case 270:
                        position[0] += value

    return abs(position[0]) + abs(position[1])


def second_star(data: list[tuple[str, int]]) -> int:
    position: list[int] = [0, 0]
    waypoint: list[int] = [1, 10]
    direction: int = 0

    for instruction, value in data:
        match instruction:
            case "N":
                waypoint[0] += value
            case "S":
                waypoint[0] -= value
            case "E":
                waypoint[1] += value
            case "W":
                waypoint[1] -= value
            case "R":
                for _ in range(value % 360 // 90):
                    waypoint[0], waypoint[1] = -waypoint[1], waypoint[0]
            case "L":
                for _ in range(value % 360 // 90):
                    waypoint[0], waypoint[1] = waypoint[1], -waypoint[0]
            case "F":
                position[0] += waypoint[0] * value
                position[1] += waypoint[1] * value

    return abs(position[0]) + abs(position[1])


if __name__ == '__main__':
    data: list[tuple[str, int]] = list()
    file_name: str = "input.txt"
    read_file(file_name, data)

    print(first_star(data))
    print(second_star(data))
