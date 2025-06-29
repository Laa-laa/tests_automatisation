import locale
from ohce import OHCE
from langues import FR, EN
from periode import Horloge


class App:
    def __init__(self):
        lang_code = locale.getlocale()[0]
        if lang_code and lang_code.startswith("fr"):
            langue = FR
        else:
            langue = EN

        horloge = Horloge()
        self.ohce = OHCE(langue=langue, horloge=horloge)

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