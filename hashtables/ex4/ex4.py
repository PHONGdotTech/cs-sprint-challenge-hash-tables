def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    cache = {}
    for number in a:
        if number < 0 and number not in cache:
            cache[number] = number

    for each in cache:
        if (cache[each] * -1) in a:
            result.append(cache[each] * -1)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
