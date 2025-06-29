class FakeHorloge:
    def __init__(self, période):
        self._période = période

    def periode(self):
        return self._période
