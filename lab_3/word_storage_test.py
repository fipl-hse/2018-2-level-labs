import unittest

from lab_3.main import WordStorage


class WordStorageTest(unittest.TestCase):
    """Check word storage class functionality"""

    def test_word_storage_put_ideal(self):
        """word is added to storage"""
        ws = WordStorage()
        word = 'word'
        num = ws.put(word)
        self.assertEqual(ws.storage[word], num)

    def test_word_storage_put_word_none(self):
        """none is not added to storage"""
        ws = WordStorage()
        word = None
        num = ws.put(word)
        self.assertEqual(ws.storage, {})

    def test_word_storage_put_word_not_str(self):
        """non string word is not added to storage"""
        ws = WordStorage()
        word = 123
        num = ws.put(word)
        self.assertEqual(ws.storage, {})

    def test_word_storage_put_existing(self):
        """existing word is not added to storage"""
        ws = WordStorage()
        word = 'word'
        ws.storage = {'word': 1}
        num = ws.put(word)
        self.assertEqual(ws.storage, {'word': 1})

    def test_word_storage_get_id_of_ideal(self):
        """ideal case for get_id_of"""
        ws = WordStorage()
        ws.storage = {'word': 1}
        self.assertEqual(ws.get_id_of('word'), 1)

    def test_word_storage_get_id_of_none(self):
        """get_id_of none"""
        ws = WordStorage()
        ws.storage = {'word': 1}
        self.assertEqual(ws.get_id_of(None), -1)

    def test_word_storage_get_id_of_not_str(self):
        """id is not str  get_id_of"""
        ws = WordStorage()
        ws.storage = {'word': 1}
        self.assertEqual(ws.get_id_of(123), -1)

    def test_word_storage_get_id_of_word_not_in_storage(self):
        """word not in storage"""
        ws = WordStorage()
        ws.storage = {'word': 1}
        self.assertEqual(ws.get_id_of('another'), -1)

    def test_word_storage_get_original_by_ideal(self):
        """ideal case for get_original_by"""
        ws = WordStorage()
        ws.storage = {'word': 1}
        self.assertEqual(ws.get_original_by(1), 'word')

    def test_word_storage_get_original_by_not_in_storage(self):
        """id not in storage get_original_by"""
        ws = WordStorage()
        ws.storage = {'word': 1}
        self.assertEqual(ws.get_original_by(2), 'UNK')

    def test_word_storage_get_original_id_none(self):
        """ideal case for get_id_of"""
        ws = WordStorage()
        ws.storage = {'word': 1}
        self.assertEqual(ws.get_original_by(None), 'UNK')

    def test_word_storage_get_original_id_not_num(self):
        """ideal case for get_id_of"""
        ws = WordStorage()
        ws.storage = {'word': 1}
        self.assertEqual(ws.get_original_by(None), 'UNK')

    def test_word_storage_from_corpus_ideal(self):
        """ideal case for get_id_of"""
        ws = WordStorage()
        sentence = ('<s>', 'mary', 'wanted', 'to', 'swim', '</s>')
        ws.from_corpus(sentence)
        self.assertEqual(len(ws.storage), 6)

    def test_word_storage_from_corpus_duplicates(self):
        """ideal case for get_id_of"""
        ws = WordStorage()
        sentence = ('<s>', 'mary', 'wanted', 'to', 'to', 'swim', '</s>')
        ws.from_corpus(sentence)
        self.assertEqual(len(ws.storage), 6)

    def test_word_storage_from_corpus_empty(self):
        """ideal case for get_id_of"""
        ws = WordStorage()
        sentence = ()
        ws.from_corpus(sentence)
        self.assertEqual(ws.storage, {})

    def test_word_storage_from_corpus_none(self):
        """ideal case for get_id_of"""
        ws = WordStorage()
        sentence = None
        ws.from_corpus(sentence)
        self.assertEqual(ws.storage, {})

    def test_word_storage_from_corpus_not_tuple(self):
        """ideal case for get_id_of"""
        ws = WordStorage()
        sentence = 'Mary wanted to swim'
        ws.from_corpus(sentence)
        self.assertEqual(ws.storage, {})
