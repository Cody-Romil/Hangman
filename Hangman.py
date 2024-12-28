import random as rd
import os 

class Hangman():
    def __init__(self):
        self.chances = 0
        self.guessed = []
        self._get_wrd()
        self._print()
        self._mainloop()

    def _get_wrd(self):
        with open(f"{os.getcwd()}/Hangman/Words.txt", "r") as file:
            self.data = file.read()
            self.wrd_list = self.data.split("\n")
            self.wrd = rd.choice(self.wrd_list)
            self.chances = 7
        print(self.wrd)
    
    def _print(self):
        for i in self.wrd:
            if i.lower() in self.guessed:
                print(i, end="")
            else:
                print("_", end="")
        print("")

    def _mainloop(self):
        print(f"Your Have {self.chances} chances to guess the word.")
        while (self.chances > 0):
            let = input("Guess a letter: ").lower()
            if let in self.wrd.lower():
                
                print("Your Guess Was Correct!")
                self.guessed.append(let)
                self._print()
            else:
                self.chances-=1
                print("Your Guess Was Incorrect!")
                print(f"You Have Only {self.chances} Chances left!")


if __name__=="__main__":
    Hangman()