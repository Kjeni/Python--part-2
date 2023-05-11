from os import path
import string

def words_count(text):
    words= text.split()
    word_count = len(words)

    word_endings = {}
    for word in words:
        clean_word = word.strip(string.punctuation)
        if clean_word:
            last_letter = clean_word[-1].lower()
            word_endings[last_letter] = word_endings.get(last_letter, 0) +1
    return word_count, word_endings

dir_path = path.dirname(__file__)
filename = "tekst.txt"
data_path = path.join(dir_path, filename)

totalwords = 0
with open(data_path, "r", encoding= "utf-8") as f:
    file_lines = f.readlines()
    
for line in file_lines[:5]:
    line_word_count, line_word_endings= words_count(line)
    totalwords += words_count(line)



print(f"Liczba słów w 3 liniach: {totalwords}")