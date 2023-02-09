import random


def exercise_1():
    name = input("Podaj swoje imię: ")
    last_name = input("a teraz nazwisko: ")
    name = name.strip(" ")
    last_name = last_name.strip(" ")
    print(f"Nazywasz się {name} {last_name}, miło Cię poznać")


def exercise_2():
    id_code = random.randint(0, 99)
    id_code = str(id_code).zfill(5)
    print(id_code)


def exercise_3():
    colors = input("Podaj swoje ulubione kolory")
    if colors.find("niebieski") > -1:
        print("Jednym z twoich ulubionych kolorów jest niebieski")
    else:
        print("Nie lubisz niebieskiego?")


def exercise_4():
    name = input("Podaj swoje imię: ")
    last_name = input("a teraz nazwisko: ")
    name = name.strip(" ")
    last_name = last_name.strip(" ")
    print("Nazywasz się {name} {last_name}, miło Cię poznać".format(name=name, last_name=last_name))


if __name__ == "__main__":
    exercise_4()
