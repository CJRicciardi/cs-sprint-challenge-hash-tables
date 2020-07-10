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