def je_int(prompt, upozorneni):
    """
    Vyžádá uživatelský vstup, ověří zda je to to interger, pokud není, nechá uživatele vstup zadat znova
    param prompt: Prompt pro uživatelský vstup
    :param upozorneni: Text upozornění, který se zobrazí pokud uživatel nezadá int
    :return:vrací číslo zadané uživatelem jako int
    """

    opakovat = True
    while opakovat:
        try:
            promenna = int(input(prompt))
            opakovat = False
        except ValueError as e:
            print(upozorneni)
    return promenna

def str_neni_prazdny(prompt, upozorneni):
    """
        Vyžádá uživatelský vstup, ověří zda vstup obsahuje alespon jeden znak, pokud ne, vyžádá vstup znovu
        :param prompt: Prompt pro uživatelský vstup
        :param upozorneni: Text upozornění, který se zobrazí pokud uživatel nezadá žádný znak
        :return: vrací uživatelský vstup jako str
        """
    opakovat = True
    while opakovat:
        str = input(prompt)
        if not str:
            print(upozorneni)
        else:
            opakovat = False
    return str

