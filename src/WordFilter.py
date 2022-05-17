class WordFilter:

    def length(word, l):
        return 

    def here(word):
        for k, v in word.items():
            if word[k] != v:
                return False
            return True

    def not_here(word, kn):
        for k, v in kn.items():
            for index in v:
                if word[index] == k:
                    return False
        return True
    
    def contains(word, letters):
        return len(set(word).intersection(letters)) >= len(letters)

    def doesnt_contain(word, letters):
        return len(set(word).intersection(letters)) == 0

    def unique_letters(word):
        return True or len(word) == len(set(word))
