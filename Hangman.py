import random as rd
import os 

class Hangman():
    def __init__(self):
        os.system("cls")
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
        self.display = ""
        for i in self.wrd:
            if i.lower() in self.guessed:
                self.display+=i
            else:
                self.display+="_"

        print(self.display, "\n")
        
        match self.chances:
            case 7:
                print("|=============\n|\n|\n|\n|\n|\n|=============\n")
            case 6:
                print("|=============\n|      |\n|\n|\n|\n|\n|=============\n")
            case 5:
                print("|=============\n|      |\n|      O\n|\n|\n|\n|=============\n")
            case 4:
                print("|=============\n|      |\n|      O\n|      |\n|\n|\n|=============\n")
            case 3:
                print("|=============\n|      |\n|      O\n|     /|\n|\n|\n|=============\n")
            case 2:
                print("|=============\n|      |\n|      O\n|     /|\\\n|\n|\n|=============\n")
            case 1:
                print("|=============\n|      |\n|      O\n|     /|\\\n|     /\n|\n|=============\n")
            case 0:
                print("|=============\n|      |\n|      O\n|     /|\\\n|     / \\\n|\n|=============\n")
                print("Sorry, You Lost The Game!")
                exit()

    def _mainloop(self):
        print(f"Your Have {self.chances} chances to guess the word.")
        while (self.chances > 0):
            let = input("Guess a letter: ").lower()
            os.system("cls")

            if let in self.wrd.lower():
                if let in self.guessed:
                    print("You Already Guesssed it!, Try another letter.")
                    self._print()
                    continue
                print("Your Guess Was Correct!")
                self.guessed.append(let)
                self._print()

            else:
                self.chances-=1
                print("Your Guess Was Incorrect!")
                print(f"You Have Only {self.chances} Chances left!")
                self._print()

            if self.display == self.wrd:
                print("You Won!")
                exit()



if __name__=="__main__":
    Hangman()