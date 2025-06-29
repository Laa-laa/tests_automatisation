from datetime import datetime
from src.ohce import OHCE

class App:
    def __init__(self):
        self.ohce = OHCE()

    def saluer(self) -> str:
        hour = datetime.now().hour
        if 5 < hour < 18:
            return "Bonjour"
        return "Bonsoir"

    def once(self):
        user_input = input("> ")
        print(self.ohce.Palindrome(user_input))

    def run(self):
        salutation = self.saluer()
        print(salutation)
        while True:
            try:
                self.once()
            except (KeyboardInterrupt, EOFError):
                break

if __name__ == "__main__":
    App().run()
