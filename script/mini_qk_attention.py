import numpy as np

Q = np.array(
    [
        [1.0, 0.0],
        [0.0, 1.0],
    ]
)

K = np.array(
    [
        [0.9, 0.1],
        [0.2, 0.8],
    ]
)

scores = Q @ K.T

print(scores)
print(scores.shape)

# Questions
#
# Why do we use `K.T`?
#
# Why is the result `2 x 2`?
#
# query 1 vs key 1
# query 1 vs key 2
# query 2 vs key 1
# query 2 vs key 2
#
# Which token best matches the first query?
# K token
#
# tips
#
# .T = transpose
#
# A = np.array([
#     [1, 2, 3],
#     [4, 5, 6]
# ])
# A.T
#
# [1 4]
# [2 5]
# [3 6]
