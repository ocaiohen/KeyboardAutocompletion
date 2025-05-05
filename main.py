import statisticsMethods
import phraseMethods

def main():
    statisticsMethods.load_file()
    print("Escreva sua frase e aperte 'enter' para receber o autocomplete da próxima palavra. Caso queira uma sequência de autocompletes apenas continue pressionando 'enter'.")
    print("Insira !0!0! para parar o programa")

    previous_phrase = ""
    while True:
        new_phrase = input("")
        if new_phrase == "!0!0!":
            break
        full_phrase = f"{previous_phrase} {new_phrase}"
        full_phrase = phraseMethods.basic_input_treatment(full_phrase)

        print(full_phrase + "\n")
        full_phrase = f"{full_phrase} {statisticsMethods.get_autocomplete_word(full_phrase)}"
        previous_phrase = full_phrase

        print(full_phrase + "\n")





main()