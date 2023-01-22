def compareTriplets(a, b):
    points_a = 0
    points_b = 0
    for i in range(3):
        if a[i] > b[i]:
            points_a += 1
        elif a[i] < b[i]:
            points_b += 1
    return [points_a, points_b]
Lucía=[100,46,53]
Carlos=[80,36,100]