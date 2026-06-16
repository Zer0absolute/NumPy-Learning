import numpy as np

query = np.array([1.0, 0.0])
key_subject = np.array([0.9, 0.1])
key_other = np.array([0.1, 0.9])

score_subject = query @ key_subject
score_other = query @ key_other

print(score_subject)
print(score_other)


# question
#
# Which score is the highest?
# result: score_subject
# explanation: score_subject is the highest because it has a higher dot product with the query
#
# Which key is most aligned with the query?
# result: key_subject
# explanation: key_subject has a higher dot product with the query than key_other, so it is most aligned with the query
#
# Why is this useful for attention?
# explanation: this is useful for attention because it allows the model to focus on the most aligned key when computing attention weights
