import random as rd
import os 

class Hangman():
    def __init__(self):
        self.chances = 0
        self._get_wrd()
        self._print()
        self._mainloop()

    def _get_wrd(self):
        with open(f"{os.getcwd()}/Hangman/Words.txt", "r") as file:
            self.data = file.read()
            self.wrd_list = self.data.split("\n")
            self.wrd = rd.choice(self.wrd_list)
            self.chances = len(self.wrd) + 2
        print(self.wrd)
    
    def _print(self):
        pass

    def _mainloop(self):
        print(f"Your Have {self.chances} chances to guess the word.")
        while (self.chances > 0):
            let = input("Guess a letter: ")
            if let in self.wrd:
                pass
            else:
                self.chances-=1


if __name__=="__main__":
    Hangman()