year = int(input())
count = 0

if year - 1600 < 0:
    print('Invalid Num')

for _ in range(year - 1600 - 1):
    if year // 4 and year % 4 == 0:
        count = count + 1
    if year // 100 and year % 100 == 0 and year // 400 and year % 400 == 0:
        count = count + 1
    year = year - 1


print(count)
