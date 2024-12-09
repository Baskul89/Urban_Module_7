class WordsFinder:
    def __init__(self, *files: str):
        self.__files = files

    def get_all_words(self):
        all_words = {}
        marks = [',', '.', '=', '!', '?', ';', ':', ' -']
        for file_name in self.__files:
            with open(file_name, 'r', encoding='utf-8') as file:
                s = file.read().lower()
                for mark in marks:
                    s = s.replace(mark,"")
                s = s.replace('\n', " ")

                all_words[file_name] = s.split(' ')

        return all_words

    def find(self, word):
        all_words = self.get_all_words()
        all_pos = {}
        for name, words in all_words.items():
            all_pos[name] = all_words[name].index(word.lower()) + 1

        return all_pos

    def count(self, word):
        all_words = self.get_all_words()
        all_counts = {}

        for name, words in all_words.items():
            all_counts[name] = all_words[name].count(word.lower())

        return all_counts



finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего