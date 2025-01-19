import unittest
import numpy as np
from topsis.topsis import Topsis

class TestTopsis(unittest.TestCase):
    def setUp(self):
        self.data = np.array([
            [250, 16, 12, 5],
            [200, 18, 8, 3],
            [300, 14, 16, 4],
            [275, 17, 10, 4],
            [225, 15, 14, 2]
        ])
        self.weights = [0.25, 0.25, 0.25, 0.25]
        self.impacts = ['+', '+', '+', '-']

    def test_ranking(self):
        topsis = Topsis(self.data, self.weights, self.impacts)
        ranks, scores = topsis.rank()
        self.assertEqual(len(ranks), len(self.data))
        self.assertTrue((scores >= 0).all() and (scores <= 1).all())
