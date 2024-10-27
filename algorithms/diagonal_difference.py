def diagonal_difference(arr):
    left = 0
    right = 0

    for i in range(len(arr)):
        # arr[0][0] + arr[1][1] + arr[2][2]
        left += arr[i][i]
        # arr[0][2] + arr[1][1] + arr[2][0]
        right += arr[i][(len(arr) - 1) - i]

    return abs(left - right)
    


data = [ [11, 2, 4], [4, 5, 6], [10, 8, -12] ]

print(diagonal_difference(data))