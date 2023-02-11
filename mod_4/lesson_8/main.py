from collections import namedtuple


def exercise_1():
    Apple = namedtuple("Apple", ["species", "size", "unit_price"])
    apple_1 = Apple("Lobo", 0.8, 4.5)
    apple_2 = Apple("Jonagold", 0.9, 11)
    apple_3 = Apple("Idared", 1.1, 8.4)

    print(apple_1.species)
    print(apple_2[1])
    for field in apple_3:
        print(field)


if __name__ == "__main__":
    exercise_1()
