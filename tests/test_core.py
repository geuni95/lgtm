import unittest

class LgtmTest(unittest.TestCase):

    def test_lgtm2(self):
        from lgtm.core import lgtm
        self.assertIsNone(lgtm())

    def test_lgtm(self):
        from lgtm.core import lgtm
        self.assertIsNone(lgtm('./python.jpeg', 'LGTM'))