import json
import os
import random
import globalVariables

words_statistics_file_name = globalVariables.STATISTICS_FILE_IN_USAGE
# with open(f"{words_statistics_file_name}.json", mode="W")

word_data = {}
def load_file():
    global word_data
    if not os.path.isfile(f"{words_statistics_file_name}.json"):
        with open(f"{words_statistics_file_name}.json", "w") as f:
            json.dump({}, f)
    
    with open(f"{words_statistics_file_name}.json", "r", encoding="utf-8") as file:
        word_data = json.load(file)
def save_file():
    with open(f"{words_statistics_file_name}.json", "w") as file:
        json.dump(word_data, file, indent=4)
def update_word_data(word, next_word, n):
    if word not in word_data:
        word_data[word] = {}
    if next_word not in word_data[word]:
        word_data[word][next_word] = 0

    word_data[word][next_word] += n
def get_autocomplete_word(phrase):
    words_list = phrase.split()
    last_word = words_list[-1]

    if last_word not in word_data.keys():
        word_data[last_word] = {}
        return random.choice(list(word_data.keys()))

    words_and_frequency = list(
        zip(word_data[last_word].keys(), word_data[last_word].values())
    )

    if words_and_frequency == []:
        # retorna uma palavra aleatória caso o words_and_frequency esteja vazio. Isso significa que a palavra está registrada no dict (pois passou pelo outro if do last_word not in word_data.keys() ) mas não tem palavras sucessoras registradas.
        return random.choice(list(word_data.keys()))

    total_sum = sum(word[1] for word in words_and_frequency)
    random_num = random.random() * total_sum

    for word, freq in words_and_frequency:
        random_num -= freq
        if random_num <= 0:
            return word
