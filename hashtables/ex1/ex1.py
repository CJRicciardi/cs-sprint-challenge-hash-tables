def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}

    done = False
    index = 1
    answer = None
    # count = 1

    # return print(reverse)


    # if len(weights) == 1:
    #     if weights[0] <= limit:
    #         answer = []
    #         answer.append(weights[0])
    #         return answer
    #     else:
    #         return answer
    if len(weights) <= 1:
        return answer
    else:
        answer = []
        def test(x, y):
            z = None
            # count = 0
            for i in range(len(x)):
                for j in range(len(x)):
                    if i != j:
                        cache[(i, j)] = x[i] + x[j]
                        z = x[i] + x[j]
                        if y == cache[(i, j)]:
                            return i, j
                    else:
                        pass           

        i, j = test(weights, limit)

        numbers = []

        if weights[i] > weights[j]:
            numbers.append(weights[j])
            numbers.append(weights[i])
        else:
            numbers.append(weights[i])
            numbers.append(weights[j])

        first = numbers[0]
        second = numbers[1]
        answer.append(weights.index(first))
        answer.append(weights.index(second))
        return answer