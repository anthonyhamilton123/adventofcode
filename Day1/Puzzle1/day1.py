def day1() -> (int, int):
    lines = read_file("input.txt")

    def part1(depths) -> int:
        return sum(1 for i, next_elem in zip(depths, depths[1:] + [depths[0]]) if i < next_elem)

    def part2(depths) -> int:
        depths = [depths[i:i+3] for i in range(0, len(depths))]
        return sum(1 for i, next_elem in zip(depths, depths[1:] + [depths[0]]) if sum(i) < sum(next_elem))

    return part1(lines), part2(lines)


def read_file(file_name: str) -> [int]:
    with open(file_name, "r") as file:
        return [int(i) for i in file.read().split()]


if __name__ == "__main__":
    print("Part 1: %d, Part 2: %d" % day1())