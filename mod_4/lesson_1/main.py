import math
import random
from math import ceil, floor


def main():
    floats = []
    for _ in range(0, 6):
        floats.append(random.uniform(-10, 20))
    print(floats)

    ints = []
    for _ in range(0, 3):
        ints.append(random.randint(1, 10))
    print(ints)

    print(round(floats[0]))
    print(ceil(floats[1]))
    print(floor(floats[2]))

    print(floats[3] ** ints[0])
    print(pow(floats[4], ints[1]))
    print(math.pow(floats[5], ints[2]))


if __name__ == "__main__":
    main()
