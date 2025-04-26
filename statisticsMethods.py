import json
import os
import random

words_statistics_file_name = "words_statistics"
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

    if last_word not in word_data:
        word_data[last_word] = {}
        return random.choice(list(word_data.keys()))
    
    words_and_frequency = list(zip(word_data[last_word].keys(), word_data[last_word].values()))

    max_frequency = max(word[1] for word in words_and_frequency)

    most_frequent_words = [word for word, freq in words_and_frequency if freq == max_frequency]

    return random.choice(most_frequent_words)

    # words_and_frequency = sorted(words_and_frequency, key = lambda x: x[1])

    # return words_and_frequency[-1][0]
    