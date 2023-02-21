def exercise_1():
    ans = input(f"Podaj pierwsze trzy litery imienia: ")
    try:
        if len(ans) != 3:
            raise ValueError(f"Na pewno wpisałeś 3 litery?")
    except ValueError:
        print(f"Chyba coś się nie udało")
    else:
        print(f"Gratulacje")
    finally:
        print(f"To już koniec")


def main():
    exercise_1()


if __name__ == "__main__":
    main()
