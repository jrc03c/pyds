import unittest
from python_data_science_helpers import chop
from numpy.random import *

class ChopTestCase(unittest.TestCase):
  def test(self):
    a = random() + 1
    self.assertEqual(chop(a), a, msg="Cannot chop a positive number!")

    b = -1 - random()
    self.assertEqual(chop(b), b, msg="Cannot chop a negative number!")

    self.assertEqual(chop(0), 0, msg="Cannot chop zero!")
    self.assertEqual(chop(1e-20), 0, msg="Cannot chop a very small positive number!")
    self.assertEqual(chop(-(1e-20)), 0, msg="Cannot chop a very small negative number!")
