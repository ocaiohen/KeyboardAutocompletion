import string
import phraseMethods
import statisticsMethods

words_dict = {}
forbidden_characters = []
forbidden_characters.extend(string.punctuation)
def main():
    statisticsMethods.load_file()
    print("Insira !0!0! para parar o programa")
    phrase = ""
    while True:
        phrase = input("")
        if phrase == "!0!0!":
            break
        phrase = phraseMethods.basic_input_treatment(phrase)
        
        phrase = phraseMethods.remove_forbidden_characters(phrase)

        phraseMethods.learn_phrase(phrase)
    
    statisticsMethods.save_file()
        
            

main()
