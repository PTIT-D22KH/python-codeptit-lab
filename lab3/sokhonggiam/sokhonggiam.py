def check(s):
    curr = s % 10
    x = s
    while (x > 0):
        digit = x % 10
        if digit > curr:
            return False
        curr = digit
        x //= 10
    return True
for _ in range(int(input())):
    s = int(input())
    if (check(s)):
        print("YES")
    else:
        print("NO")