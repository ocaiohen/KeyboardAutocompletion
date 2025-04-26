import json
import os

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
    print(word_data)