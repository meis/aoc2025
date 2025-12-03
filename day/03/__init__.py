def part1(input):
    total_output_joltage = 0

    for line in input:
        total_output_joltage += _get_bank_joltage(line, 2)

    return total_output_joltage


def part2(input):
    total_output_joltage = 0

    for line in input:
        total_output_joltage += _get_bank_joltage(line, 12)

    return total_output_joltage


def test():
    assert _get_bank_joltage("987654321111111", 2) == 98
    assert _get_bank_joltage("811111111111119", 2) == 89
    assert _get_bank_joltage("234234234234278", 2) == 78
    assert _get_bank_joltage("818181911112111", 2) == 92

    assert _get_bank_joltage("987654321111111", 3) == 987
    assert _get_bank_joltage("811111111111119", 3) == 819
    assert _get_bank_joltage("234234234234278", 3) == 478
    assert _get_bank_joltage("818181911112111", 3) == 921

    assert _get_bank_joltage("987654321111111", 12) == 987654321111
    assert _get_bank_joltage("811111111111119", 12) == 811111111119
    assert _get_bank_joltage("234234234234278", 12) == 434234234278
    assert _get_bank_joltage("818181911112111", 12) == 888911112111


def _get_bank_joltage(bank: str, digits=2) -> int:
    joltage: str = ""
    last_max = -1

    for current_digit in range(digits):
        start = last_max + 1
        end = len(bank) - (digits - current_digit) + 1

        current_digit = max(bank[start:end])
        last_max = bank.find(current_digit, start, end)

        joltage += current_digit

    return int(joltage)
