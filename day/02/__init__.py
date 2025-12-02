def part1(input):
    invalids = 0

    for id_range in input:
        invalids += _sum_invalids(id_range, _is_valid)

    return invalids


def part2(input):
    invalids = 0

    for id_range in input:
        invalids += _sum_invalids(id_range, _is_really_really_valid)

    return invalids


def test():
    assert _is_valid(12)
    assert not _is_valid(11)
    assert not _is_valid(123123)
    assert _is_really_really_valid(1234)
    assert not _is_really_really_valid(12341234)
    assert not _is_really_really_valid(123123123)
    assert not _is_really_really_valid(1212121212)
    assert not _is_really_really_valid(1111111)
    assert _sum_invalids("11-22", _is_valid) == 33
    assert _sum_invalids("95-115", _is_valid) == 99
    assert _sum_invalids("1698522-1698528", _is_valid) == 0


def _sum_invalids(id_range: str, method) -> int:
    (start, end) = id_range.split("-")
    sum_invalids = 0

    for i in range(int(start), int(end) + 1):
        if not method(i):
            sum_invalids += i

    return sum_invalids


def _is_valid(num: int):
    return _is_partible_by(num, 2)


def _is_really_really_valid(num: int):
    return _is_partible_by(num, 2, 3, 5, 7, 9, 13)


def _is_partible_by(num: int, *num_partitions):
    as_str = str(num)
    for partition in num_partitions:
        if partition > len(as_str):
            break
        if as_str == as_str[: (len(as_str) // partition)] * partition:
            return False

    return True
