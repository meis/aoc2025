from typing import Tuple

Ingredient = int
Range = Tuple[int, int]


def part1(input):
    (ranges, ingredients) = _parse_input(input)

    fresh_ingredients = 0

    for ingredient in ingredients:
        if any([i[0] <= ingredient <= i[1] for i in ranges]):
            fresh_ingredients += 1

    return fresh_ingredients


def part2(input):
    (ranges, _) = _parse_input(input)

    total_fresh_ingredients = 0

    for merged_range in ranges:
        total_fresh_ingredients += merged_range[1] - merged_range[0] + 1

    return total_fresh_ingredients


def test():
    assert _extend_range_set([(1, 2), (3, 4)], (2, 3)) == [(1, 4)]
    assert _extend_range_set([(1, 2), (3, 4)], (5, 6)) == [(1, 2), (3, 4), (5, 6)]


def _parse_input(input) -> Tuple[list[Range], list[Ingredient]]:
    ranges: list[Range] = []
    ingredients: list[Ingredient] = []

    crossed_the_line = False
    for line in input:
        if line == "":
            crossed_the_line = True
            continue

        if crossed_the_line:
            ingredients.append(int(line))
        else:
            (start, end) = line.split("-")
            ranges = _extend_range_set(ranges, (int(start), int(end)))

    return ranges, ingredients


def _extend_range_set(range_set: list[Range], range: Range) -> list[Range]:
    new_range_set = []
    to_merge = [range]

    for elem in range_set:
        if elem[0] <= range[1] and elem[1] >= range[0]:
            to_merge.append(elem)
        else:
            new_range_set.append(elem)

    new_range_set.append(
        (
            min(to_merge, key=lambda x: x[0])[0],
            max(to_merge, key=lambda x: x[1])[1],
        )
    )

    return new_range_set
