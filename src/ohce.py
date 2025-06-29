class OHCE:
    def __init__(self, langue, horloge):
        self.langue = langue
        self.horloge = horloge

    def Palindrome(self, input_str: str) -> str:
        période = self.horloge.periode()
        reversed_str = input_str[::-1]
        parts = [self.langue.bonjour(période), reversed_str]

        if input_str == reversed_str:
            parts.append(self.langue.bien_dit)

        parts.append(self.langue.au_revoir(période))
        return "\n".join(parts)
