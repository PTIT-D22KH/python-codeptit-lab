a = []
with open("DATA.in", "r") as file:
    b = file.readlines()
    for c in b:
        s = c.split()
        for x in s:
            # print(x)
            if (len(x) >= 10):
                a.append(x)
                continue
            try:
                t = int(x)
            except:
                a.append(x)
a.sort()
for x in a:
    print(x, end = ' ')