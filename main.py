import bintrees


class Translation:
    def __init__(self, word: str, usage_example = None):
        self.word = word
        if usage_example is not None:
            self.usage_example = usage_example
        else:
            self.usage_example = ""

    def __str__(self):
        return f"Translation: {self.word}. Usage example: {self.usage_example}"

class WordCouples:
    def __init__(self, word: str):
        self.word = word
        self.translations = {}
        # self.usage_example =

    def add_translation(self, trans_word: str, usage_example = None):
        this_translation = Translation(trans_word, usage_example)
        self.translations[trans_word] = this_translation

    def delete_translation(self, trans_word):
        self.translations.pop(trans_word)

    def __str__(self):
        all_translations = ", ".join(self.translations)
        all_usage_examples = ""

        for t in self.translations.values():
            all_usage_examples += str(t) + ", "

        return f"Word: {self.word}. Translations: {all_translations}. Usage example: {all_usage_examples}"


class Dictionary:
    def __init__(self):
        self.words = bintrees.AVLTree()

    def add_word(self, word: str):
        this_word = WordCouples(word)
        self.words.insert(key=word, value=this_word)

    def delete(self, word: str):
        if word in self.words:
            self.words.remove(word)

    def add_translation(self, key_word: str, translation: str, usage_example = None):
        if key_word in self.words:
            self.words[key_word].add_translation(translation)
            return

        print(f"No {key_word} in the dictionary found")

    def delete_translation(self, key_word, translation: str):
        if key_word in self.words:
            self.words[key_word].delete_translation(translation)

    def display_word(self, key_word: str):
        if key_word in self.words:
            print(self.words[key_word])
            return

        print(f"No {key_word} in the dictionary found")


dict1 = Dictionary()

dict1.add_word("Apple")
dict1.add_translation("Apple", "Яблоко")
dict1.add_translation("Apple", "Яблочко")

dict1.add_word("Word")
dict1.add_translation("Word", "Слово")

dict1.delete("Word")

dict1.display_word("Apple")
dict1.display_word("Word")

dict1.delete_translation("Apple", "Яблочко")
dict1.display_word("Apple")