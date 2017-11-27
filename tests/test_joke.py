from unittest import TestCase

import zufaelliger

class TestJoke(TestCase):
    def test_is_string(self):
        s = zufaelliger.joke()
        self.assertTrue(isinstance(s, basestring))

