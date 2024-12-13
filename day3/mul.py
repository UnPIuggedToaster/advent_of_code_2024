import re
import sys
from copy import deepcopy
import ast

def part1(ls: list[str]) -> int:

    nums = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', ''.join(ls))
    return sum([(int(x[0]) * int(x[1])) for x in nums])

def part2(ls: list[str]) -> int:
    return part1(re.sub(r'don\'t\(\).*?do\(\)', '', ''.join(ls)))


if __name__ == "__main__":
    fname = sys.argv[1] if len(sys.argv) > 1 else 'input'
    f = [l.strip() for l in open(fname)]
    print("Part 1: ", part1(deepcopy(f)))
    print("Part 2: ", part2(deepcopy(f)))