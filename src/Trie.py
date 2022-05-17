test_words = "i am just writing some random words that hopefully have the same root im amex justify writer son wordy thanos hop hat having theater samuel room"
test_words = test_words.split(" ")

class Trie:
    def __init__(self, words):
        self.root = {}
        self.end = "_end_"
        for word in words:
            current = self.root
            for char in word:
                current = current.setdefault(char, {})
            current[self.end] = self.end
    
    def __repr__(self):
        return str(self.root)
    
    def __str__(self):
        raise NotImplementedError("use repr, havent thought of a good way to print this yet.")
    
    def __contains__(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                return False
            current = current[letter]
        return self.end in current

    
a = Trie((word for word in test_words))
print("writing" in a)