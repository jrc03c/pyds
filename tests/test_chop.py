import unittest
from python_data_science_helpers import chop
from numpy.random import *

class ChopTest(unittest.TestCase):
  def test(self):
    a = random() + 1
    self.assertEqual(chop(a), a)

    b = -1 - random()
    self.assertEqual(chop(b), b)

    self.assertEqual(chop(0), 0)
    self.assertEqual(chop(1e-20), 0)
