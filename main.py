from evidence import Evidence
from overeni import je_int

print(
    "_______________________________________________________\nEVIDENCE POJIŠTĚNCŮ\n_______________________________________________________")

print("Možné akce:\n1 - přidat pojištěnce\n2 - zobrazit všechny pojištěnce \n3 - vyhledat pojištěnce \n4 - ukončit program")
evidence = Evidence()

run = True
while run:
    volba_operace = je_int("\nProsím zadejte číslo akce, kterou chcete provést\n", "To není číslo")

    if volba_operace == 1:
        evidence.zadej_noveho_pojistence()
    elif volba_operace == 2:
        evidence.zobraz_pojistene()
    elif volba_operace == 3:
        evidence.vyhledej_pojistence()
    elif volba_operace == 4:
        print("Aplikace se nyní zavře")
        quit()
    else:
        print("prosím zadejte platné číslo akce")


