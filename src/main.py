from src.ohce import OHCE
from src.langues import FR

class App:
    def __init__(self):
        self.ohce = OHCE(langue=FR)  # On injecte la langue ici

    def once(self):
        user_input = input("> ")
        print(self.ohce.Palindrome(user_input))

    def run(self):
        while True:
            try:
                self.once()
            except (KeyboardInterrupt, EOFError):
                break

if __name__ == "__main__":
    App().run()
