# Perdaryti biudzeto programa su klasémis (is 6 paskaitos) taip, kad visos klases büty skirtinguose failuose.



import pickle

from modules.biudzetas import Biudzetas

FILE_NAME = "biudzetas.pkl"


try:
    with open(FILE_NAME, "rb") as f:         #isikeliam senus duomenis
      biudzetas = pickle.load(f)
except FileNotFoundError:
      biudzetas = Biudzetas()                  # Jei failo nėra, pradedame su tuščiu sąrašu

def issaugoti_duomenis(biudzetas):
      with open(FILE_NAME, "wb") as f:            # issisaugom ivestus duomenis i failiuka
          pickle.dump(biudzetas, f)

while True:
    print("******** BIUDZETAS ***")
    print("1 - Pridėti pajamas")
    print("2 - Pridėti išlaidas")
    print("3 - Pajamu ir islaidu balansas")
    print("4 - Parodyti ataskaita")
    print("5 - Išeiti")

    pasirinkimas = input("Pasirinkite veiksmą: ")

    if pasirinkimas == "1":
        suma = float(input("Ivesti pajamu suma: "))
        siuntejas = input("Ivesti siunteja: ")
        papildoma_informacija = input("Ivesti papildoma info: ")
        biudzetas.prideti_pajamu_isras(suma, siuntejas, papildoma_informacija)   #susidedam pajamas i biudzeto zurnala
        issaugoti_duomenis(biudzetas)                                             # issisaugom i agurkeli 
    elif pasirinkimas == "2":
        suma = float(input("Ivesti islaidu suma: "))
        atsiskaitymo_budas = input("Atsiskaitymo budas: ")
        isigyta_preke_paslauga = input("Isigyta preke/paslauga: ")
        biudzetas.prideti_islaidos_isras(suma, atsiskaitymo_budas, isigyta_preke_paslauga)
        issaugoti_duomenis(biudzetas)
    elif pasirinkimas == "3":
        print(f"Balansas: {biudzetas.gauti_balansa()} EUR")                   #atsiprintinam biudzeta
    elif pasirinkimas == "4":
        biudzetas.parodyti_ataskaita()                                        # atsiprintinam ataskaita
    elif pasirinkimas == "5":
        print("Programa baigta.")                                             # susinaikinam
        break
    else:
        print("Neteisingas pasirinkimas, bandykite dar kartą.")

    print("\n")
