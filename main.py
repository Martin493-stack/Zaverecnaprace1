from evidence import Evidence
from logo import Logo
print(Logo)
def main():
    evidence = Evidence()

    while True:
        print("\n----- EVIDENCE POJISTENYCH -----")
        print("1. Vytvořit pojištěného")
        print("2. Zobrazit seznam pojištěných")
        print("3. Vyhledat pojištěného")
        print("4. Konec")

        volba = input("Zvolte možnost (1-4): \n")

        if volba == "1":
            evidence.vytvor_pojisteneho()
        elif volba == "2":
            evidence.zobraz_seznam_pojisteny()
        elif volba == "3":
            evidence.vyhledej_pojisteneho()
        elif volba == "4":
            print("Děkujeme za využití naší aplikace.")
            break
        else:
            print("Neplatná volba.")


if __name__ == "__main__":
    main()






