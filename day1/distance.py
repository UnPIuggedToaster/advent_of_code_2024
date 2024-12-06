import sys
from collections import Counter
from copy import deepcopy


def part1 (f: list[str]) -> int:
    arr1, arr2 = zip(*f)
    arr1 = list(map(int, arr1))
    arr2 = [int(x) for x in arr2]

    return sum([abs(a - b) for a,b in zip(sorted(arr1), sorted(arr2))])


def part2 (f: list[str]) -> int:
    arr1, arr2 = zip(*f)
    arr1 = list(map(int, arr1))
    arr2 = list(map(int, arr2))
    return sum([i * Counter(arr2)[i] for i in arr1])


if __name__ == "__main__":
    fname = sys.argv[1] if len(sys.argv) > 1 else 'input'
    f = [l.strip().split() for l in open(fname)]
    print("Part 1: ", part1(deepcopy(f)))
    print("Part 2: ", part2(deepcopy(f)))

