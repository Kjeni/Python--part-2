from os import path

def word_count(text):
    words= text.split()
    return len(words)

dir_path = path.dirname(__file__)
filename = "tekst.txt"
data_path = path.join(dir_path, filename)

totalwords = 0
with open(data_path, "r", encoding= "utf-8") as f:
    file_lines = f.readlines()
    
for line in file_lines[:5]:
    totalwords += word_count(line)

print(f"Liczba słów w 3 liniach: {totalwords}")