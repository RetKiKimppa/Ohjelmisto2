from classes.auto import Sähköauto, Polttomoottoriauto

if __name__ == "__main__":
    tesla = Sähköauto("ABC-123", 180, 52.5)
    volvo = Polttomoottoriauto("XYZ-221", 165, 32.3)

    tesla.kiihdyta(90)
    volvo.kiihdyta(125)

    tesla.kulje(3)
    volvo.kulje(3)

    print(f"Tesla: {tesla.matka}km")
    print(f"Volvo: {volvo.matka}km")