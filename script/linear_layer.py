import numpy as np

x = np.array(
    [
        [1.0, 2.0],
    ]
)

W = np.array(
    [
        [2.0, 0.0, 1.0],
        [0.0, 3.0, 1.0],
    ]
)

y = x @ W

print(x.shape)
print(W.shape)
print(y)
print(y.shape)

# Questions
#
# What is the shape of `x`? 1x2
# What is the shape of `W`? 2x3
# What is the shape of `y`? 1x3
# Why does the result have 3 dimensions?
# response: the result has 3 dimensions because `x` has 1 row and 2 columns, `W` has 2 rows and 3 columns, and `y` has 1 row and 3 columns.
#
# tips
# shape = number of rows * number of columns
#
# french :
# La shape décrit l’organisation des données (lignes, colonnes, axes).
# La dimension d’un vecteur décrit le nombre de composantes qu’il contient.
