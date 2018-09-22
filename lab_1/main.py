""""
Labour work #1

Count frequencies dictionary by the given arbitrary text
"""
text = '''The semantic field of any town is an interesting and diversified totality of different onyms which have a certain meaning given by a nominator. At the same time such system is strictly territorial, therefore it should be considered with its historical, ethnic, natural and other features of the area. The special characteristic of these objects is the social significance because they are the crucial reference point for a person in the urban environment. Onomastics is one of the sections of lexicology which studies onyms, the history of their emergence and transformations as a result of the long usage in the source language or in connection with their borrowing.
Ergonomics is the special branch of onomastics. Ergonyms are the researching objects of ergonomics. They mean names of various business associations of people.  For the first time this term was declared by N.V. Podolskaya in “The Dictionary of Russian Onomastic Terminology”. Thanks to it, this notion has firmly consolidated in onomastics.  Ergonomic lexis as any system of onyms is characterized with a number of features.'''
stopwords = ['onomastics', 'the', 'onym']
calculate_frequency(text)
filter_stop_words(frequent_dict, stopwords)
get_top_n(frequent_dict, n)


def calculate_frequences() -> dict:
        """
        Calculates number of times each word appears in the text
        """
        pass

def filter_stop_words() -> dict:
        """
        Removes all stop words from the given frequencies dictionary
        """
        pass

def get_top_n() -> tuple:
        """
        Takes first N popular words
        """
        pass
