import json
import sys
from difflib import get_close_matches, SequenceMatcher
class Dictionary:
    def __init__(self):
        self.data = json.load(open("./data.json"))
    
    def meaning_of_word(self,w):
        if w.lower() in self.data:
            w = w.lower()
            return self.pretty_print(w)
        elif w.upper() in self.data:
            w = w.upper()
            return self.pretty_print(w)
        else:
            return self.return_closest_match(w)

    def return_closest_match(self,w):
        try:
            w_match, *_ = get_close_matches(w,self.data.keys())
        except:
            return "Sorry try a different word!"
        print("Sorry, that word doesn't exist. Did you mean: {0}?".format(w_match))
        choice_user_1 = input("Enter Y or N: ").lower()
        if choice_user_1 == 'y':
            return self.pretty_print(w_match)
        else:
            return "Sorry try a different word!"
    
    def pretty_print(self,w):
        return '\n'.join(self.data[w])
    
    
def user_choice():
    print('''
    Type 1: Enter a word 
    Type 2: Quit''')
    try:
        choice = int(input("Enter choice: 1 or 2 "))
        if choice == 1:
            word = input("Enter the word you would like to know the meaning of: ")
            print(dict.meaning_of_word(word))
            user_choice()
        if choice == 2:
            exit_program()
    except (ValueError):
        print("Invalid input\n")
        user_choice() 
    else:
        print("Enter a valid choice: 1 or 2: ")
        user_choice()

def exit_program():
    print("\nGoodbye!\n")
    exit()

if __name__ == "__main__":
    dict = Dictionary()
    print('''
    ====================== WELCOME TO THE COMMAND LINE DICTIONARY TOOL ======================
                           !Disclaimer: Not everyone knows everything!
    =======================================================================================''')
    user_choice()
