class OHCE:
    def __init__(self, langue):
        self.langue = langue

    def Palindrome(self, input_str: str) -> str:
        reversed_str = input_str[::-1]
        parts = [self.langue.bonjour, reversed_str]

        if input_str == reversed_str:
            parts.append(self.langue.bien_dit)

        parts.append(self.langue.au_revoir)
        return "\n".join(parts)
