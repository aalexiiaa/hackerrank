def plus_minus(arr):
    positive_count, negative_count, zero_count = 0, 0, 0
    length = len(arr)

    for x in arr:
        if x > 0:
            positive_count += 1
        elif x < 0:
            negative_count += 1
        else:
            zero_count += 1

    print(positive_count / length)
    print(negative_count / length)
    print(zero_count / length)

plus_minus([-4, 3, -9, 0, 4, 1])