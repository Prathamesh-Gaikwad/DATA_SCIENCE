
def distance_sum(x, y, n):
    _sum = 0
    for i in range(n):
        for j in range((i+1), n):
            _sum = _sum + abs(x[i] - x[j]) + abs(y[i] - y[j])

    return _sum


x = [-1, 1, 3, 2]
y = [5, 6, 5, 3]
n = len(x)

print(distance_sum(x, y, n))
