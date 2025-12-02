import sys
import os
import importlib.util

if len(sys.argv) < 2:
    print("Usage: python -m day <day_number> [input_file]")
    print("       default input_file: 'input'")
    sys.exit(1)

day_num = sys.argv[1].zfill(2)  # Pad with zeros
input_file = sys.argv[2] if len(sys.argv) > 2 else "input"

# Load the day module from directory
day_dir = os.path.join(os.path.dirname(__file__), day_num)
day_file = os.path.join(day_dir, "__init__.py")
spec = importlib.util.spec_from_file_location(f"day{day_num}", day_file)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# Read input
input_path = os.path.join(day_dir, input_file)
with open(input_path) as f:
    input_data = f.read().splitlines()
if len(input_data) == 1:
    input_data = input_data[0].split(",")

# Run test if it exists
if hasattr(module, 'test'):
    module.test()

# Call part1 and part2 if they exist
if hasattr(module, 'part1'):
    print("Part 1:", module.part1(input_data))
else:
    print("Part 1: Not implemented")

if hasattr(module, 'part2'):
    print("Part 2:", module.part2(input_data))
else:
    print("Part 2: Not implemented")
