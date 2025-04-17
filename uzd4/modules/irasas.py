


class Irasas:
    def __init__(self, tipas, suma):    
        self.tipas = tipas                                       # finansai = pajamos ar islaidos
        self.suma = suma              

    def __str__(self):                                                   # prisidedam __str__ metoda, grazina objekto teksta.
        return f"{self.tipas}: {self.suma} EUR"                        # pvz. "pajamos: 100 eur"
    