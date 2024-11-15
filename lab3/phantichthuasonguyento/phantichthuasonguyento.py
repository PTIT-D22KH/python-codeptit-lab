import math
for _ in range(int(input())):
    n = int(input())
    print("1", end = '')
    for i in range(2, int(math.sqrt(n)) + 1):
        count = 0
        while n % i == 0:
            count += 1
            n /= i
        if count >= 1:
            print(f" * {i}^{count}", end = '')
    if (n > 1):
        print(f" * {int(n)}^1", end = '')
    print()
