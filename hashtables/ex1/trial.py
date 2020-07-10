from ex1 import get_indices_of_item_weights

iterations = 1

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

# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# y = 14

# def test(x, y):
#     z = None
#     count = 0
#     for i in range(len(x)):
#         for j in range(len(x)):
#             count += 1
#             print('Count:', count)
#             z = x[i] + x[j]
#             if y == z:
#                 return i, j            

# i, j = test(x, y)

# if x[i] < x[j]:
#     return [x[j], x[i]]
# else:
#     return x[i], x[j]