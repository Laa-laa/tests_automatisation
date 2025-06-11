from datetime import datetime

class App:
    def saluer(self) -> str:
        hour = datetime.now().hour
        if 5 < hour < 18:
            return "Bonjour"
        return "Bonsoir"
        
    def mirror(self, text: str) -> str:
        return text[::-1]

    def once(self):
        user_input = input("> ")
        print(self.mirror(user_input))

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
