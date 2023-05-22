from pojisteni import Pojisteny


class Evidence:
    def __init__(self):
        self.pojisteni = []

    def vytvor_pojisteneho(self):
        while True:
            jmeno = input("Zadejte jméno: ").capitalize()
            prijmeni = input("Zadejte příjmení: ").capitalize()
            vek = input("Zadejte věk: ")
            telefon = input("Zadejte telefonní číslo: ")

            if not vek.isdigit() or not telefon.isdigit():
                print("Chybný vstup. Věk a telefon musí obsahovat pouze číselné hodnoty.")
                return
            if len(telefon) != 9:
                print("Chybný vstup. Telefon musí mít 9 znaků.")
                return

            pojisteny = Pojisteny(jmeno, prijmeni, vek, telefon)
            self.pojisteni.append(pojisteny)
            print("Pojištěný byl vytvořen.")
            volba = input("1. Zadat dalšího pojištěnce ? \n2. Návrat do hlavní nabídky\nZvolte možnost (1-2): ")
            if volba == "1":
                continue
            elif volba == "2":
                break

    def zobraz_seznam_pojisteny(self):
        if not self.pojisteni:
            print("V seznamu není žádný pojištěnec.")
        else:
            for pojisteny in self.pojisteni:
                print(pojisteny)

    def vyhledej_pojisteneho(self):
        jmeno = input("Zadejte jméno: ").capitalize()
        prijmeni = input("Zadejte příjmení: ").capitalize()

        nalezeno = False
        for pojisteny in self.pojisteni:
            if pojisteny.jmeno == jmeno and pojisteny.prijmeni == prijmeni:
                print(pojisteny)
                nalezeno = True
                break

        if not nalezeno:
            print("Pojištěný nebyl nalezen.")
