class Langue:
    def __init__(
        self,
        bonjour_am, bonjour_pm, bonjour_soir, bonjour_nuit,
        au_revoir_am, au_revoir_pm, au_revoir_soir, au_revoir_nuit,
        bien_dit
    ):
        self.salutations = {
            "matin": bonjour_am,
            "après-midi": bonjour_pm,
            "soirée": bonjour_soir,
            "nuit": bonjour_nuit,
        }
        self.adieux = {
            "matin": au_revoir_am,
            "après-midi": au_revoir_pm,
            "soirée": au_revoir_soir,
            "nuit": au_revoir_nuit,
        }
        self.bien_dit = bien_dit

    def bonjour(self, période):
        return self.salutations[période]

    def au_revoir(self, période):
        return self.adieux[période]


FR = Langue(
    bonjour_am="Bonjour",
    bonjour_pm="Bonjour",
    bonjour_soir="Bonsoir",
    bonjour_nuit="Bonsoir",
    au_revoir_am="Bonne journee",
    au_revoir_pm="Bonne apres midi",
    au_revoir_soir="Bonne soiree",
    au_revoir_nuit="Bonne nuit",
    bien_dit="Bien dit!"
)

EN = Langue(
    bonjour_am="Good morning",
    bonjour_pm="Good afternoon",
    bonjour_soir="Good evening",
    bonjour_nuit="Good night",
    au_revoir_am="Bye morning",
    au_revoir_pm="Bye afternoon",
    au_revoir_soir="Bye evening",
    au_revoir_nuit="Bye night",
    bien_dit="Well said!"
)
