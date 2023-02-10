from random import randint


def add_element_to_frozenset(frozenset_old):
    new_element = frozenset({randint(0, 10)})
    return frozenset.union(frozenset_old, new_element)


def add_element_to_set(set_old):
    new_element = set({randint(0, 10)})
    return set_old.union(new_element)


def exercise_1():
    frozenset_1 = frozenset({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10})
    frozenset_2 = frozenset()
    i = 0
    while frozenset_2 != frozenset_1:
        frozenset_2 = add_element_to_frozenset(frozenset_2)
        print(frozenset_2)
        i += 1
    print(f"Udało się po {i} iteracjach")


def exercise_2():
    set_1 = set({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10})
    set_2 = set()
    i = 0
    while set_2 != set_1:
        set_2 = add_element_to_set(set_2)
        print(set_2)
        i += 1
    print(f"Udało się po {i} iteracjach")


if __name__ == "__main__":
    exercise_2()
