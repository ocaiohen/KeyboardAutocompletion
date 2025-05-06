import phraseMethods
import statisticsMethods
import trainingMethods
import globalVariables

def main():
    statisticsMethods.load_file()

    print("Insira 0 caso queira carregar o arquivo .txt do whatsapp")
    print("Insira 1 caso queira treinar o autocomplete com o terminal")
    
    op = input().strip()
    if op == "0":
        print("Carregando arquivo .txt do whatsapp...")
        trainingMethods.learn_from_whatsapp_chat_file(globalVariables.WHATSAPP_TXT_GROUP_FILE_IN_USAGE, globalVariables.WHATSAPP_TXT_GROUP_SPECIFIC_CONTACT)
    elif op == "1":
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
