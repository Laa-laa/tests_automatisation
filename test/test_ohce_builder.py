from src.ohce import OHCE
from src.langues import FR, EN


class OHCEBuilder:
    def __init__(self):
        self.langue = FR

    def parlant(self, langue):
        self.langue = langue
        return self

    def build(self):
        return OHCE(self.langue)
