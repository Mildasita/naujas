
from modules.islaidu_irasas import IslaiduIrasas
from modules.pajamu_irasas import PajamuIrasas

class Biudzetas:
    def __init__(self):   
        self.zurnalas = []                                                 # susikuriam zurnala, kur matysis visos pajamos ir islaidos


    def prideti_pajamu_isras (self, suma, siuntejas, papildoma_informacija):   
        irasas = PajamuIrasas (suma, siuntejas, papildoma_informacija)
        self.zurnalas.append(irasas)

    def prideti_islaidos_isras (self, suma, atsiskaitymo_budas, isigyta_preke_paslauga):
        irasas = IslaiduIrasas (suma, atsiskaitymo_budas, isigyta_preke_paslauga)
        self.zurnalas.append(irasas)

    def gauti_balansa(self):            # susiskaiciuojam visas pajamas(isl) is zurnalo,pereinam su isinstance per classe, jei pajamos isitraukiam i suma
        pajamos = sum(irasas.suma for irasas in self.zurnalas if isinstance(irasas, PajamuIrasas))
        islaidos = sum(irasas.suma for irasas in self.zurnalas if isinstance(irasas, IslaiduIrasas))
        return pajamos - islaidos

    def parodyti_ataskaita(self):               # atsprintinan ataskaita (irasu zurnala)
        for irasas in self.zurnalas:   
            print(irasas)

