def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    for index in range(len(weights)):
        if (weights[index] not in cache) and (limit - weights[index] in weights):
            cache[weights[index]] = index

    if len(cache) == 2:
        first = None
        second = None
        for weight in cache:
            if first == None:
                first = cache[weight]
            else:
                second = cache[weight]
        if first > second:
            return (first, second)
        else:
            return (second, first)
    elif len(cache) == 1:
        first = None
        second = None
        for index in range(len(weights)):
            if weights[index] in cache:
                if first == None:
                    first = index
                else:
                    second = index

        if first > second:
            return (first, second)
        else:
            return (second, first)


    return None

if __name__ == "__main__":
    print(get_indices_of_item_weights([9], 1, 9))
    print(get_indices_of_item_weights([ 4,4], 2, 8))
    print(get_indices_of_item_weights([ 4, 6, 10, 15, 16 ], 5, 21))
    print(get_indices_of_item_weights([12, 6, 7, 14, 19, 3, 0, 25, 40], 9, 7))
