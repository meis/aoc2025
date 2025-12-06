from typing import Literal, Tuple
from dataclasses import dataclass


@dataclass
class Problem:
    symbol: Literal["+", "*"]
    numbers: list[int]

    def solve(self) -> int:
        if not self.numbers:
            return 0
        if self.symbol == "+":
            return sum(self.numbers)
        else:
            total = 1
            for n in self.numbers:
                total *= n
            return total


def part1(input):
    problems = _parse_input_human(input)

    return sum([problem.solve() for problem in problems])


def part2(input):
    problems = _parse_input_celphalopod(input)

    return sum([problem.solve() for problem in problems])


def _parse_input_human(input) -> list[Problem]:
    problems = []

    homework = [i.split() for i in input]
    symbols = homework.pop()
    homework = [[int(i) for i in row] for row in homework]

    for col in range(len(symbols)):
        exercice = Problem(symbols[col], [])

        for row in range(len(homework)):
            exercice.numbers.append(int(homework[row][col]))

        problems.append(exercice)

    return problems

def _parse_input_celphalopod(input) -> list[Problem]:
    symbols_line = input.pop()
    problem_coords: list[Tuple[Literal["+", "*"], list[int]]] = []

    for i in range(len(symbols_line)):
        character = symbols_line[i]
        if character != " ":
            problem_coords.append((character, []))
        problem_coords[-1][1].append(i)

    problems = []
    for coords in problem_coords:
        problem = Problem(coords[0], [])

        for i in coords[1]:
            number_string_representation = ""

            for line in input:
                if line[i] != " ":
                    number_string_representation += line[i]

            if number_string_representation:
                problem.numbers.append(int(number_string_representation))

        problems.append(problem)

    return problems
