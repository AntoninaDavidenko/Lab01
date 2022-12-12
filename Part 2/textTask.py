
with open('Example.txt', 'r') as f:
    text = f.read()


class Operations:

    def __init__(self, text_two):
        self.text = text_two

    def count_letters(self):
        letters = 0
        for letter in self.text:
            if letter.isalpha():
                letters += 1
        print("Total letters:", letters)

    def count_words(self):
        words = self.text.split()
        print("Total words:", len(words))

    def sentences_count(self):
        print("Total sentences:", text.count("."))


ex = Operations(text)
ex.count_letters()
ex.count_words()
ex.sentences_count()
