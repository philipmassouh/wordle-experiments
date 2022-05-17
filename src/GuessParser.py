from collections import defaultdict
import copy

from WordFilter import WordFilter

class GuessParser():
    def __init__(self, length: int) -> None:
        self.length = length
        self.desired_letters = set()
        self.excluded_letters = set()
        self.known = {} # 0:"s"
        self.knownnot = {} # "s":set()
    
    def _gray(self,l):
        self.excluded_letters.add(l)

    def _yellow(self,i,l):
        self.desired_letters.add(l)
        self.knownnot.setdefault(l,set()).add(i)
        
    def _green(self,i,l):
        self.desired_letters.add(l)
        self.known.setdefault(i,l)

    def _add_guess(self, guess: str) -> None:
        g = iter(guess)
        for i,letter in enumerate(g):
            if letter == "!":
                self._gray(next(g).lower())
            elif letter.islower():
                self._yellow(i, letter.lower())
            else:
                self._green(i, letter.lower())

    def __repr__(self):
        return (
            f"{self.length}\n"
            f"{self.desired_letters}\n"
            f"{self.excluded_letters}\n"
            f"{self.known}\n"
            f"{self.knownnot}"
        )

    def parse_guess(self, guess: str):
        self._add_guess(guess)
        return (
            copy.deepcopy(self.length),
            copy.deepcopy(self.desired_letters),
            copy.deepcopy(self.excluded_letters),
            copy.deepcopy(self.known),
            copy.deepcopy(self.knownnot)
        )

g = GuessParser(5)
print(g.parse_guess("!rAT!i!o"))
print(g.parse_guess("!s!h!r!u!b"))
print(g.parse_guess("E!i!g!ht"))


