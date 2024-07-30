import re
from collections import Counter

def count_words(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
        words = re.findall(r'\b\w+\b', content.lower())
        word_count = Counter(words)
        return word_count

def display_top_words(word_count, n):
    top_words = word_count.most_common(n)
    for word, count in top_words:
        print(f'{word}: {count}')

file_name = 'example.txt'  # replace with your file name
word_count = count_words(file_name)
display_top_words(word_count, 10)  # display top 10 words