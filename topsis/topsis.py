import numpy as np
import pandas as pd

class Topsis:
    def __init__(self, data, weights, impacts):
        self.data = data
        self.weights = np.array(weights)
        self.impacts = np.array(impacts)

    def normalize(self):
        norm = np.sqrt((self.data ** 2).sum(axis=0))
        self.normalized_data = self.data / norm

    def weighted_normalization(self):
        self.weighted_data = self.normalized_data * self.weights

    def ideal_best_worst(self):
        self.ideal_best = np.where(self.impacts == '+', 
                                   self.weighted_data.max(axis=0), 
                                   self.weighted_data.min(axis=0))
        self.ideal_worst = np.where(self.impacts == '+', 
                                    self.weighted_data.min(axis=0), 
                                    self.weighted_data.max(axis=0))

    def calculate_distances(self):
        self.distance_best = np.sqrt(((self.weighted_data - self.ideal_best) ** 2).sum(axis=1))
        self.distance_worst = np.sqrt(((self.weighted_data - self.ideal_worst) ** 2).sum(axis=1))

    def calculate_scores(self):
        self.scores = self.distance_worst / (self.distance_best + self.distance_worst)

    def rank(self):
        self.normalize()
        self.weighted_normalization()
        self.ideal_best_worst()
        self.calculate_distances()
        self.calculate_scores()
        ranks = (-self.scores).argsort() + 1
        return ranks, self.scores
