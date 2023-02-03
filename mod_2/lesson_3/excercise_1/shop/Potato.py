class Potato:
    def __init__(self, species, size, price_per_kg):
        self.species = species
        self.size = size
        self.price_per_kg = price_per_kg
        self.full_price = 0

    def calculate_full_price(self, amount_in_kg):
        self.full_price = self.price_per_kg * amount_in_kg
        print(f"Cena za {amount_in_kg} kilogramów ziemniaków gatunku {self.species} o rozmiarze {self.size} "
              f"wynosi {self.full_price} PLN")
