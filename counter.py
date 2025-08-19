from collections import defaultdict
import json
import string


file_path = input("Enter file path: ")

try:
    with open(file_path, 'r') as file_input:
        text = file_input.read().lower()
except FileNotFoundError:
    print("The file was not found.")
    exit()

text = text.translate(str.maketrans('', '', string.punctuation))

count = defaultdict(int)

for char in text.split():
    count[char] += 1



print(sorted(count.items(), key=lambda x:x[1]))
        

