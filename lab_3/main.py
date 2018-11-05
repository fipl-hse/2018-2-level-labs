"""
Labour work #3
 Building an own N-gram model
"""
from random import randint

REFERENCE_TEXT = '''Mar#y wa$&nted, to swim! However, she was afraid of sharks. Afl kj.
asd, aeqw, owei. Kjm KJH! Fqwe! Andrew, Lida, Nina, Andrew , Lida< Ninaa fq swim, however. Nine people died in the incident in Casteldaccia - from children aged one, three and 15 to their grandparents. Only three people who were outside the house at the time survived.
Three other people died when their cars were swept away elsewhere in Sicily.
Days of heavy rain and winds have killed at least 17 other people in Italy, mainly in the north and west.
Some of the worst damage was to roads around Belluno in the northern Veneto region, after days of storms had dislodged mud, rocks and water.
Twelve members of two families had gathered to spend the night when water from river Milicia swamped the house.
Three of those on the premises had lucky escapes.
The father of one of the children - and another child - had gone out on an errand at the time. Of the other 10, one was outside and survived climbing on to a tree.
In addition to the three children, the dead included the mother of two of them, two grandparents, their son and daughter, and another woman.
One of the neighbours described the scene minutes before the incident.
"I heard the dogs barking. It was around 22:30 (21:30 GMT). I told my husband to go out to see what was happening. He opened the door and water filled the house," said Maria Concetta Alfano.It’s hard to imagine now, but there was a time when humans only had access to sugar for a few months a year when fruit was in season. Some 80,000 years ago, hunter-gatherers ate fruit sporadically and infrequently, since they were competing with birds.
Now, our sugar hits come all year round, often with less nutritional value and far more easily – by simply opening a soft drink or cereal box. It doesn’t take an expert to see that our modern sugar intake is less healthy than it was in our foraging days. Today, sugar has become public health enemy number one: governments are taxing it, schools and hospitals are removing it from vending machines and experts are advising that we remove it completely from our diets.
But so far, scientists have had a difficult time proving how it affects our health, independent of a diet too high in calories. A review of research conducted over the last five years summarised that a diet of more than 150g of fructose per day reduces insulin sensitivity – and therefore increases the risk of developing health problems like high blood pressure and cholesterol levels. But the researchers also concluded that this occurs most often when high sugar intake is combined with excess calories, and that the effects on health are "more likely" due to sugar intake increasing the chance of excess calories, not the impact of sugar alone.
Meanwhile, there is also a growing argument that demonising a single food is dangerous – and causes confusion that risks us cutting out vital foods.
Sugar, otherwise known as ‘added sugar’, includes table sugar, sweeteners, honey and fruit juices, and is extracted, refined and added to food and drink to improve taste.
But both complex and simple carbohydrates are made up of sugar molecules, which are broken down by digestion into glucose and used by every cell in the body to generate energy and fuel the brain. Complex carbohydrates include wholegrains and vegetables. Simple carbohydrates are more easily digested and quickly release sugar into the bloodstream. They include sugars found naturally in the foods we eat, such as fructose, lactose, sucrose and glucose and others, like high fructose corn syrup, which are manmade.
You might also like:
Before the 16th Century only the rich could afford sugar. But it became more available with colonial trade.
Then, in the 1960s, the development of large-scale conversion of glucose into fructose led to the creation of high fructose corn syrup, a concentrate of glucose and fructose.
This potent combination, above any other single type of sugar, is the one many public health advocates consider the most lethal – and it is the one that many people think of when they think of ‘sugar’.'''


# ШАГ 1. Разбиение текста и токенизация
def split_by_sentence(text: str) -> list:
    new_text = ''
    list_of_marks = [
        '.', ',', ':', '"', '`', '[', ']',
        '?', '!', '@', '&', "'", '-',
        '$', '^', '*', '(', ')',
        '_', '“', '”', '’', '#', '%', '<', '>', '*', '~',
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
    ]
    good_marks = ['.', '!', '...', '?']
    result_list = list()

    for index, element in enumerate(text):
        try:
            if element in good_marks and text[index + 2].isupper():
                try:
                    new_text += '.' + text[index + 1]
                    continue
                except IndexError:
                    pass
        except IndexError:
            pass
        if element in list_of_marks:
            continue
        new_text += element
    sentences_list = new_text.split('. ')

    for sentence in sentences_list:
        sentence = sentence.lower()
        splitted = sentence.split()
        result_list.append(splitted)

    return result_list


# ШАГ 2. Создание хранилища
class WordStorage:
    def __init__(self):
        self.counter = 0
        self.word_id_dict = dict()

    def put(self, word: str) -> int:
        self.word_id_dict[word] = self.counter
        self.counter += 1
        return self.word_id_dict[word]

    def get_id_of(self, word: str) -> int:
        if word not in self.word_id_dict:
            return None
        return self.word_id_dict[word]

    def get_original_by(self, id: int) -> str:
        if id not in self.word_id_dict.values():
            return None
        for word, word_id in self.word_id_dict.items():
            if word_id == id:
                return word

    def from_corpus(self, corpus: tuple) -> str:
        for sentence in corpus:
            for word in sentence:
                if word in self.word_id_dict:
                    continue
                self.word_id_dict[word] = self.counter
                self.counter += 1
        return 'OK'


# ШАГ 3. Кодирование корпуса/списка предложений
def encode(storage_instance, corpus) -> list:
    encoded_list = list()
    for sentence in corpus:
        inner_list = list()
        for word in sentence:
            inner_list.append(storage_instance[word])
        encoded_list.append(inner_list)
    return encoded_list


raw_storage = WordStorage()


raw_storage.from_corpus(tuple(split_by_sentence(REFERENCE_TEXT)))
raw_storage.put('<s>')
raw_storage.put('</s>')

encoded_text = encode(raw_storage.word_id_dict, split_by_sentence(REFERENCE_TEXT))

print(raw_storage.word_id_dict)
print(encoded_text)


class NGramTrie:
    def __init__(self, scale: int):
        self.size = scale
        self.gram_frequencies = dict()
        self.gram_log_probabilities = dict()

    def fill_from_sentence(self, sentence: tuple) -> str:
        list_of_grams_one_sentence = list()
        for index, word in enumerate(sentence):
            if len(sentence) <= 1:
                list_of_grams_one_sentence.append((raw_storage.get_id_of('<s>'), word))
                list_of_grams_one_sentence.append((word, raw_storage.get_id_of('</s>')))
                break
            if index == 0:
                list_of_grams_one_sentence.append((raw_storage.get_id_of('<s>'), word))
                list_of_grams_one_sentence.append((word, sentence[index + 1]))
                continue
            if index == len(sentence) - 1:
                list_of_grams_one_sentence.append((word, raw_storage.get_id_of('</s>')))
                break
            list_of_grams_one_sentence.append((word, sentence[index + 1]))
        print(list_of_grams_one_sentence)
        for gram in list_of_grams_one_sentence:
            if gram in self.gram_frequencies:
                continue
            for encoded_sentence in encoded_text:
                for index, encoded_word in enumerate(encoded_sentence):
                    if index == len(encoded_sentence) - 1:
                        break
                    if (gram[0] == encoded_word) and (gram[1] == encoded_sentence[index + 1]):
                        self.gram_frequencies[gram] = self.gram_frequencies.get(gram, 0) + 1
        return 'OK'


print(len(encoded_text))
NGram_raw = NGramTrie(2)
NGram_raw.fill_from_sentence(encoded_text[randint(1, 20)])
print(NGram_raw.gram_frequencies)
