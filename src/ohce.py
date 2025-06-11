class OHCE:

    def Palindrome(self, input_str: str) -> str:
        greeting = "bonjour"
        reversed_str = input_str[::-1]
        parts = [greeting, reversed_str]

        if input_str == reversed_str:
            parts.append("Bien dit!")

        parts.append("au revoir")
        return "\n".join(parts)
