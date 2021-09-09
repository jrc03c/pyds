import unittest
from python_data_science_helpers import correl
from numpy import *
from numpy.random import *

class CorrelTestCase(unittest.TestCase):
  def test(self):
    a = random(size=999999)
    b = random(size=999999)
    self.assertLess(abs(correl(a, b)), 0.01, msg="The correlation of two random vectors is NOT close to 0!")

    a = random(size=999999)
    b = a + 1e-5 * normal(size=999999)
    self.assertGreater(abs(correl(a, b)), 0.99, msg="The correlation of two almost-identical vectors is NOT close to 1!")
