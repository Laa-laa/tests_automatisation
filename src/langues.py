class Langue:
    def __init__(self, bonjour: str, au_revoir: str, bien_dit: str):
        self.bonjour = bonjour
        self.au_revoir = au_revoir
        self.bien_dit = bien_dit


FR = Langue("bonjour", "au revoir", "Bien dit!")
EN = Langue("hello", "goodbye", "Well said!")
