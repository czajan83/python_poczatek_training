from dataclasses import dataclass


@dataclass
class Apple:
    species: str
    size: str
    unit_price: float

    def __repr__(self):
        return_text = f"Apple gatunek='{self.species}', rozmiar={self.size}, cena za kilogram={self.unit_price}"
        return return_text

