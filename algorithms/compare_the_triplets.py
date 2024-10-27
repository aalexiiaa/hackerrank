def compare_triplets(a, b):
    score = [0, 0]

    for i in range(len(a)):
        if a[i] > b[i]:
            score[0] += 1
        elif a[i] < b[i]:
            score[1] += 1
    
    return score

print(compare_triplets([1, 2, 3], [3, 2, 1]))