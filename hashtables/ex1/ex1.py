def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    length = len(weights)
    hashmap = dict()

    #if length of array is less than or equal to 1 ..return None
    if length <= 1:
        return None

    # Traverse arr only once. For each weight w in arr compute its complement limit - w and check whether that
    # complement is hashed so far. If found the complement in the map, return a pair that consists of
    # w’s and limit - w’s indices. if not, hash w while using the weight as the hash key and its array index as the hash
    # value. Even if the same weight is found more than once it doesn’t matter because at the time of the lookup we only
    # need one item with that weight

    for i in range(length):
        weight = weights[i]
        if weight in hashmap:
            value = hashmap[weight]
            return [i, value]
        diff = limit - weight
        hashmap[diff] = i
    return []

    
