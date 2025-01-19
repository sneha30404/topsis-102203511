import pandas as pd
from topsis.topsis import Topsis

data = pd.read_csv('examples/example.csv')

matrix = data.iloc[:, 1:].values
weights = [0.25, 0.25, 0.25, 0.25]
impacts = ['+', '+', '+', '-']

topsis = Topsis(matrix, weights, impacts)
ranks, scores = topsis.rank()

data['Score'] = scores
data['Rank'] = ranks
print(data)
