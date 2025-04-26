import phraseMethods
import statisticsMethods

def main():
    statisticsMethods.load_file()
    print("Insira !0!0! para parar o programa")
    while True:
        phrase = input("")
        if phrase == "!0!0!":
            break
        phrase = phraseMethods.basic_input_treatment(phrase)
        
        phrase = phraseMethods.remove_forbidden_characters(phrase)

        phraseMethods.learn_phrase(phrase)
    
    statisticsMethods.save_file()

main()
