import re

def cmp(a):
    return (-d[a], a)

regex = r'[\s,.?!:;()-/]'
a = []
d = {}

for _ in range(int(input())):
    s = input().lower()
    for i in range(len(s)):
        if not s[i].isalnum():
            s = s.replace(s[i], ' ')
    s = s.split()
    # s = re.split(regex, s)
    for x in s:
        if len(x) > 0:
            if x not in d:
                d[x] = 1
            else:
                d[x] += 1

a = list(d.keys())
a.sort(key=cmp)

for x in a:
    print(f"{x} {d[x]}")