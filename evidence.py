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
