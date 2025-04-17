from modules.irasas import Irasas

class IslaiduIrasas(Irasas):
    tipas = "Islaidos"
    def __init__(self, suma, atsiskaitymo_budas, isigyta_preke_paslauga):   #I klase IslaiduIrasas papildomai pridéti 
        super().__init__(self.tipas, suma)                                  #savybes atsiskaitymo_budas ir isigyta_preke_paslauga, kurias 
        self.atsiskaitymo_budas = atsiskaitymo_budas                        # kurias, vartotojas galétu irasyti. +
        self.isigyta_preke_paslauga = isigyta_preke_paslauga


    def __str__(self):                                                      # atsiprintinam islaidu info (kiek, kaip, uz ka)
        return f"{self.tipas}: {self.suma} EUR, Būdas: {self.atsiskaitymo_budas}, Prekė/Paslauga: {self.isigyta_preke_paslauga}"

