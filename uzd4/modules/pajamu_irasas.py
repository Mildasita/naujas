from modules.irasas import Irasas


class PajamuIrasas(Irasas): 
    tipas = "Pajamos"                                            # su "Pajamos" nusirodom finansai kokia
    def __init__(self, suma, siuntejas, papildoma_informacija):           #  I klase PajamuIrasas papildomai pridéti 
        super().__init__(self.tipas, suma)                                 # savybes siuntejas ir papildoma_informacija, 
        self.siuntejas = siuntejas                                         # kurias vartotojas galétu irasyti.
        self.papildoma_informacija = papildoma_informacija                


    def __str__(self):                                                      # atsiprintinam pajamu info (kiek, is kur gauta, papil.info)
        return f"{self.tipas}: {self.suma} EUR, Siuntėjas: {self.siuntejas}, Info: {self.papildoma_informacija}"

