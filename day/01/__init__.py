def part1(input):
    current = 50
    total_times_0 = 0

    for rotation in input:
        (current, _) = _move(current, rotation)

        if current == 0:
            total_times_0 += 1

    return total_times_0


def part2(input):
    current = 50
    total_clicks_to_0 = 0

    for rotation in input:
        (current, clicks_to_0) = _move(current, rotation)

        total_clicks_to_0 += clicks_to_0

    return total_clicks_to_0


def _move(position: int, rotation: str) -> tuple[int, int]:
    direction = 1 if rotation[0] == "R" else -1
    distance = int(rotation[1:])
    total_distance = position + (direction * distance)

    clicks_to_0 = int(abs(total_distance) / 100)

    # If we went from positive (> 0) to negative, we need to add an extra 0 click
    if position != 0 and total_distance == 0:
        clicks_to_0 += 1

    current = total_distance % 100
    return (current, clicks_to_0)
