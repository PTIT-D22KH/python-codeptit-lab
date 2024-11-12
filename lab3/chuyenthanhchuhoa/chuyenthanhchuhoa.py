s = input()
res = ""
for c in s:
    if c.isalpha():
        # print(c.upper())
        c = c.upper()
    res += c
print(res)