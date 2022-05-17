import csv
import string

# dict to dict interface for storing words?best data s
# maybe replicate data 5x sorting alphabetically by each letter

# no plurals in OG

desired_letters = "de"
desired_length = 5
excluded_letters = "aiughost"
known = {}  # : "e"}  # 2:"i"}
knownnot = {"d":[1], "e":[3]}


def pos(word, known):
    for k, v in known.items():
        if word[k] != v:
            return False
    return True


def notpos(word, knownnot):
    for k, v in knownnot.items():
        for index in v:
            if word[index] == k:
                return False
    return True


def contains(word, letters):
    return len(set(word).intersection(letters)) >= len(letters)


def notcontains(word, letters):
    return len(set(word).intersection(letters)) == 0


def unique_letters(word):
    return True or len(word) == len(set(word))


def get_matches():
    for row in csv.reader(open("words_alpha.txt"), delimiter="\n"):
        word = row[0]
        if (
            len(word) == desired_length
            and unique_letters(word)
            and notpos(word, knownnot)
            and pos(word, known)
            and contains(word, set(list(desired_letters)))
            and notcontains(word, set(list(excluded_letters)))
        ):
            yield word


m = list(get_matches())
print(f"{len(m)} result(s): {m}")

# at this point, we have eliminated all things that are literally invalid
# we can make recommendations now with the remaining wordlist
# this should be wrapped in a method and called when new information is received
#       furthermore, it should be as modular as possible for generating special queries for recommendations or sparse remnants

letter_counts = {letter: 0 for letter in string.ascii_lowercase}
for word in m:
    for letter in word:
        letter_counts[letter] += 1

letter_avg_idx = {letter: 0 for letter in string.ascii_lowercase}
for word in m:
    for i, l in enumerate(word):
        letter_avg_idx[l] += i

# maybe useful for guessing
for k, v in letter_avg_idx.items():
    if v > 0:
        letter_avg_idx[k] = int(round(letter_avg_idx[k] / letter_counts[k], 5))


print(
    list(
        map(
            lambda x: x[0],
            sorted(list(letter_counts.items()), reverse=True, key=lambda x: x[1]),
        )
    )
)


# guess recommendation

# information-gathering recommendation ?

# carts
# blart
#