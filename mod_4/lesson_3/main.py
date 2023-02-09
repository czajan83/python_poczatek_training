def exercise_1():
    list_1 = [x for x in range(30) if x % 3 == 0]
    print(list_1)
    list_2 = [x for x in range(30) if x % 5 == 0]
    print(list_2)
    list_3 = list_1.copy()
    list_3.extend(list_2)
    print(list_3)


def exercise_2():
    sports = []
    sport_input = input("Podaj jakiś ulubiony sport lub wpisz X aby zakończyć")
    while sport_input != "X":
        sports.append(sport_input)
        sport_input = input("Podaj inny ulubiony sport lub wpisz X aby zakończyć")

    print(sports[1::2])


if __name__ == "__main__":
    exercise_2()
