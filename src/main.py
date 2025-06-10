class App:
    def mirror(self, text: str) -> str:
        return text[::-1]

    def once(self):
        user_input = input("> ")
        print(self.mirror(user_input))

    def run(self):
        while True:
            try:
                self.once()
            except (KeyboardInterrupt, EOFError):
                break

if __name__ == "__main__":
    App().run()
