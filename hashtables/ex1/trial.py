# # from ex1 import get_indices_of_item_weights

iterations = 1

def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    
    d = {}
    def inner(weights, length, limit):
        for i in range(length):
            for j in range(length):
                if i != j:
                    if (weights[i]+weights[j]) not in d:
                        d[weights[i]+weights[j]] = [i, j]
                    elif limit in d:
                        return d[limit]
                    else:
                        pass
    
    x = inner(weights, length, limit)

    if length < 2:
        return None
    elif x[0] < x[1]:
        x.reverse()
    
    return x




print('\n\n', iterations, '\n\n')
print(get_indices_of_item_weights([9], 1, 9))
iterations += 1
print('\n\n', iterations, '\n\n')
print(get_indices_of_item_weights([4, 4], 2, 8))
iterations += 1
print('\n\n', iterations, '\n\n')
print(get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 21))
iterations += 1
print('\n\n', iterations, '\n\n')
print(get_indices_of_item_weights([12, 6, 7, 14, 19, 3, 0, 25, 40], 9, 7))

# d = {}

# def inner(weights, length, limit):
#     for i in range(length):
#         for j in range(length):
#             if i != j:
#                 if (weights[i]+weights[j]) not in d:
#                     d[weights[i]+weights[j]] = [i, j]
#                 elif limit in d:
#                     return d[limit]
#                 else:
#                     pass

# print(inner([12, 6, 7, 14, 19, 3, 0, 25, 40], 9, 7))