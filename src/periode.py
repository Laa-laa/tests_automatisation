from datetime import datetime

class Horloge:
    def periode(self) -> str:
        hour = datetime.now().hour
        if 6 <= hour < 12:
            return "matin"
        elif 12 <= hour < 18:
            return "après-midi"
        elif 18 <= hour < 22:
            return "soirée"
        else:
            return "nuit"
