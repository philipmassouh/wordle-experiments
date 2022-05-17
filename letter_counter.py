import csv
import string
import functools

letter_counts = {letter:0 for letter in string.ascii_lowercase}
for word in csv.reader(open("words_alpha.txt"), delimiter="\n"):
    if len(word[0]) == 5:
        for letter in word[0]:
            letter_counts[letter] += 1

print(list(map(lambda x: x[0],sorted(list(letter_counts.items()), reverse=True, key=lambda x:x[1]))))

letter_counts = {letter:0 for letter in string.ascii_lowercase}
for word in csv.reader(open("words_alpha.txt"), delimiter="\n"):
    for letter in word[0]:
        letter_counts[letter] += 1

print(list(map(lambda x: x[0],sorted(list(letter_counts.items()), reverse=True, key=lambda x:x[1]))))