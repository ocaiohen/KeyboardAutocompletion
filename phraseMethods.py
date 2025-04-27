import globalVariables
import statisticsMethods

def basic_input_treatment(phrase):
    phrase = phrase.lower()
    phrase = phrase.strip()

    return phrase
def remove_forbidden_characters(phrase):
    words_list = []

    for word in phrase.split():
        characters_list = list(word)

        for i in range(len(characters_list)):
            if characters_list[i] in globalVariables.FORBIDDEN_CHARACTERS:
                if characters_list[i] == "-":
                    # Remove "-" no começo ou no final
                    if i == 0 or i == len(characters_list) - 1:
                        characters_list[i] = ""
                else:
                    characters_list[i] = ""

        word = "".join(c for c in characters_list if c != "")
        words_list.append(word)

    return " ".join(words_list)
def learn_phrase(phrase):
    words_list = phrase.split()

    for i in range(len(words_list) - 1):
        statisticsMethods.update_word_data(words_list[i], words_list[i + 1], 1)
