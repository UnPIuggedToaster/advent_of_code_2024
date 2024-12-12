import sys 
from copy import deepcopy

def check_list(ls: list[int]) -> bool:
    return all(1 <= ls[i+1] - ls[i] <= 3 for i in range(len(ls)-1)) or all(1 <= ls[i] - ls[i+1] <= 3 for i in range(len(ls)-1))


def part1(ls: list[int]) -> int:
    count = len([+1
        for sub in ls
        if (check_list(sub))
    ])
    return count


def part2(ls: list[int]) -> int:

    count = 0

    count = len([])

    # count += len([(print(x), 1)
    #               if check_list(x)
    #               else(
    #                 1
    #                 if all(check_list(x[:i] + x[i+1:]) for i in range(len(x)))
    #                 else 0
    #                 )
    #               for x in ls
    #             ])

    for x in ls:
        # if all(1 <= abs(x[i] - x[i+1]) <= 3 for i in range(len(x)-1)):
        if check_list(x):
            count += 1
            continue

        for i in range(len(x)):
            temp_list = x[:i] + x[i+1:]

            if check_list(temp_list):
                count += 1
                break

    return count


if __name__ == "__main__": 
    fname = sys.argv[1] if len(sys.argv) > 1 else 'input'
    f = [[int(num) for num in l.strip().split()] for l in open(fname)]
    print ("Part 1: ", part1(deepcopy(f)))
    print ("Part 2: ", part2(deepcopy(f)))
