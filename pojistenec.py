from overeni import je_int
from overeni import str_neni_prazdny


class Pojistenec:
    #třída pro pojištěnce
    def __init__(self):
        #konstruktor pro instanci pojitěnce, vyžádá uživatelský vstup pro zadání jmena,příjmení, věku a tel, čísla
        self.jmeno = str_neni_prazdny("Zadejte prosím křestní jméno pojištěnce: ", "Pro přidání do evidence je nutné zadat jméno")
        self.prijmeni = str_neni_prazdny("Zadejte prosím příjmení pojištěnce: ", "Pro přidání do evidence je nutné zadat příjmení")
        self.vek = je_int("Zadejte prosím věk pojištěnce: ", "Prosím zadejte věk jako číslici")
        self.telefon = input("Zadejte telefon pojištěnce: ")

    def __str__(self):
        #vrátí jméno, příjmení, věk a telefon pojištěnce jako string
        return f"jméno: {self.jmeno} příjmení: {self.prijmeni} věk: {self.vek} telefon: {self.telefon}"