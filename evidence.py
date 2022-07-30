from pojistenec import Pojistenec

class Evidence:
#Třída pro vytvoření evidence pojištěných
    def __init__(self):
        #incializace, vytvoří list seznam_pojistenych, který slouží k ukládání informací o pojištěných v aplikaci
        self.seznam_pojistenych = []

    def uloz_pojistence_na_seznam(self, novy_pojistenec):
        #uloží nového pojištěnce na seznam pojištěných
        self.seznam_pojistenych.append(novy_pojistenec)

    def zadej_noveho_pojistence(self):
        #vytvoří novou instanci pojištěne, připojí nového pojištěnce na aktuální seznam pojištěných
        print("Zadat nového pojištěnce")
        self.novy_pojistenec = Pojistenec()
        self.uloz_pojistence_na_seznam(self.novy_pojistenec)

    def zobraz_pojistene(self):
        #zobrazí aktuální seznam pojištěných, pro každého pojištěnce na seznamu zobrazí jméno, příjmení, věk a telefon
       print("Aktuální seznam pojištěných")
       for pojisteny in self.seznam_pojistenych:
            print(pojisteny)

    def vyhledej_pojistence(self):
        print("Vyhledat pojištěnce")
        jmeno = input("Zadejte křestní jméno pojištěného: ")
        prijmeni = input("Zadejte příjmení pojištěného: ")
        vysledek = ()
        for pojistenec in self.seznam_pojistenych:
            if pojistenec.jmeno == jmeno and pojistenec.prijmeni == prijmeni:
                vysledek = str(pojistenec)
        if vysledek == ():
            print("Pojiěnec nenalezen")
        else:
             print(vysledek)
"""
    def zadej_noveho_pojistence(self):
    # Nechá uživatele vyplnit informace o novém pojištěnci
        print("Zadat nové pojištěnce\n")
        jmeno = input("Zadejte prosím křestní jméno pojištěnce: ")
        prijmeni = input("Zadejte prosím příjmení pojištěnce: ")
        vek = je_int("Zadejte prosím věk pojištěnce: ", "Prosím zadejte věk jako číslici")
        telefon = input("Zadejte telefon pojištěnce: ")
        self.uloz_pojistence_na_seznam(jmeno, prijmeni, vek, telefon)
        #ulozi noveho pojistence na seznam
        print("Nový pojištěnec byl přidaný na seznam")


    def zobraz_pojistene(self):
        # zobrazí seznam všech pojištěných
        print("Aktuální seznam pojištěných:")
        for pojistenec in self.seznam_pojistenych:
           print(f"jméno: {pojistenec[0]}   příjmení:  {pojistenec[1]}   věk: {pojistenec[2]}    telefon: {pojistenec[3]}")

    
"""
