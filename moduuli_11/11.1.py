from classes.julkaisu import Kirja, Lehti

if __name__ == "__main__":
    julkaisu1 = Lehti("Aku Ankka", "Aki Hyyppä")
    julkaisu2 = Kirja("Hytti nro 6", "Rosa Liksom", 200)
    julkaisu1.tulosta_tiedot()
    julkaisu2.tulosta_tiedot()