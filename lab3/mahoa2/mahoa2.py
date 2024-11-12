p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
    s = input()
    if s == '0':
        break
    a = [i for i in s.split()]
    k = int(a[0])
    x = a[1]
    res = ""
    for i in range(len(x)):
        index = p.find(x[i])
        res += p[(index + k) % 28]
    print(res[::-1])
