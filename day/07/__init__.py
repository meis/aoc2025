def part1(input):
    (_, splitters) = _get_beams_and_splitters(input)
    return splitters


def part2(input):
    (beams, _) = _get_beams_and_splitters(input)
    return beams


def _get_beams_and_splitters(input):
    splitters = 0
    beams = [1 if x == "S" else 0 for x in input[0]]

    for line in input:
        new_beams = [0 for _ in beams]

        for i in range(len(line)):
            if line[i] == "^":
                new_beams[i - 1] += beams[i]
                new_beams[i + 1] += beams[i]

                if beams[i]:
                    splitters += 1
            else:
                new_beams[i] += beams[i]

        beams = new_beams

    return sum(beams), splitters
