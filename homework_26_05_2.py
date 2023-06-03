res = 0

for i in range(1, 10000):
    sum = 0

    for j in range(i):
        if i % (j+1) == 0:
            sum += j+1
        res = sum - i

    if res == i:
        print(res)
