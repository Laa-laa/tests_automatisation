from src.ohce import OHCE
from src.langues import FR
from fakes import FakeHorloge

class OHCEBuilder:
    def __init__(self):
        self.langue = FR
        self.période = "matin"

    def parlant(self, langue):
        self.langue = langue
        return self

    def à_la_période(self, période):
        self.période = période
        return self

    def build(self):
        horloge = FakeHorloge(self.période)
        return OHCE(self.langue, horloge)
