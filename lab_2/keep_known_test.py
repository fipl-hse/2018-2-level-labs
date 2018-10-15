import unittest

from lab_2.main import keep_known


class KeepKnownTest(unittest.TestCase):
    """
    Tests deleting unknown words from candidates
    """

    def test_keep_known_ideal(self):
        """ Ideal case """
        freq_dict = dict(list=1, lust=2)
        as_is_words = ('LYST',)
        candidates = ('lwst', 'lrst', 'list', 'lust', 'lyst')
        expected = ['list', 'lust', 'lyst']
        known = keep_known(candidates, as_is_words, freq_dict)
        self.assertCountEqual(expected, known)

    def test_keep_known_as_is_empty(self):
        """ as_is_words is empty tuple"""
        freq_dict = dict(list=1, lust=2)
        as_is_words = tuple([])
        candidates = ('lwst', 'lrst', 'list', 'lust', 'lyst')
        expected = ['list', 'lust']
        known = keep_known(candidates, as_is_words, freq_dict)
        self.assertCountEqual(expected, known)

    def test_keep_known_as_is_none(self):
        """as_is_words is None"""
        freq_dict = dict(list=1, lust=2)
        as_is_words = None
        candidates = ('lwst', 'lrst', 'list', 'lust', 'lyst')
        expected = []
        known = keep_known(candidates, as_is_words, freq_dict)
        self.assertCountEqual(expected, known)

    def test_keep_known_as_is_not_str(self):
        """as_is_words contain element that is not str"""
        freq_dict = dict(list=1, lust=2)
        as_is_words = (1, 'LYST')
        candidates = ('lwst', 'lrst', 'list', 'lust', 'lyst')
        expected = ['list', 'lust', 'lyst']
        known = keep_known(candidates, as_is_words, freq_dict)
        self.assertCountEqual(expected, known)

    def test_keep_known_as_is_word_el_none(self):
        """as_is_word contains None"""
        freq_dict = dict(list=1, lust=2)
        as_is_words = (None, 'LYST')
        candidates = ('lwst', 'lrst', 'list', 'lust', 'lyst')
        expected = ['list', 'lust', 'lyst']
        known = keep_known(candidates, as_is_words, freq_dict)
        self.assertCountEqual(expected, known)

    def test_keep_known_candidate_empty(self):
        """candidates is empty"""
        freq_dict = dict(list=1, lust=2)
        as_is_words = ('LYST',)
        candidates = ()
        expected = []
        known = keep_known(candidates, as_is_words, freq_dict)
        self.assertCountEqual(expected, known)

    def test_keep_known_candidate_none(self):
        """candidates is None"""
        freq_dict = dict(list=1, lust=2)
        as_is_words = ('LYST',)
        candidates = None
        expected = []
        known = keep_known(candidates, as_is_words, freq_dict)
        self.assertCountEqual(expected, known)

    def test_keep_known_candidate_not_str(self):
        """candidate contains el that is not str"""
        freq_dict = dict(list=1, lust=2)
        as_is_words = (None, 'LYST')
        candidates = (1, 'list', 'lust', 'lwst')
        expected = ['list', 'lust']
        known = keep_known(candidates, as_is_words, freq_dict)
        self.assertCountEqual(expected, known)

    def test_keep_known_candidates_not_tuple(self):
        """candidates type is not tuple"""
        freq_dict = dict(list=1, lust=2)
        as_is_words = (None, 'LYST')
        candidates = ['list', 'lust', 'lwst']  # should be tuple
        expected = []
        known = keep_known(candidates, as_is_words, freq_dict)
        self.assertCountEqual(expected, known)

    def test_keep_known_candidates_freq_is_empty(self):
        """freq dict is empty"""
        freq_dict = dict()
        as_is_words = (None, 'LYST')
        candidates = ('list', 'lust', 'lwst')
        expected = []
        known = keep_known(candidates, as_is_words, freq_dict)
        self.assertCountEqual(expected, known)

    def test_keep_known_candidates_freq_is_none(self):
        """freq dict is none"""
        as_is_words = (None, 'LYST')
        candidates = ('list', 'lust', 'lwst')
        expected = []
        known = keep_known(candidates, as_is_words, None)
        self.assertCountEqual(expected, known)

    def test_keep_known_candidates_freq_has_not_str(self):
        """freq dict contains key that is not str"""
        freq_dict = {1: 5, 'list': 2}
        as_is_words = (None, 'LYST')
        candidates = ('list', 'lust')
        expected = ['list']
        known = keep_known(candidates, as_is_words, freq_dict)
        self.assertCountEqual(expected, known)

    def test_keep_known_candidates_freq_all_none(self):
        """All params are None"""
        expected = []
        known = keep_known(None, None, None)
        self.assertCountEqual(expected, known)
