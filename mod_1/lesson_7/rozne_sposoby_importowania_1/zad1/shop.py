from zad1 import asortment

def place_order():
    product = input(f"Co chcesz kupić? {asortment.asortment}, X aby zakończyć ")
    whole_price = 0.0
    while product != "X":
        if not product in asortment.asortment:
            print("Nie mamy tego produktu\n")
        else:
            print(f"Dostępność tego produktu to: {asortment.availability[product]}")
            print(f"Cena tego produktu to: {asortment.prices[product]}")
            quantity = int(input("Ile sztuk tego produktu chcesz kupić? "))
            if quantity > asortment.availability[product]:
                print("Nie mamy tak dużej ilości tego produktu")
            else:
                print("Produkt dodany do koszyka")
                whole_price += quantity * asortment.prices[product]
        product = input(f"Co chcesz jeszcze kupić? {asortment.asortment}, X aby zakończyć ")
    print(f"Cena końcowa zakupów to {whole_price}")
    whole_price = 0
    return 0
