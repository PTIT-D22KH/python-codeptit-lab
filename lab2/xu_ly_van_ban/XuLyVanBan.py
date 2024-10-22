import re

a = []
regex = r'[\w\s\,\:]+'
while True:
    s = ""
    try:
        s = input()
        # print(s)
        s = s.lower().strip()
        temp = re.findall(regex, s)
        
        for x in temp:
            t = x.split()
            print(t[0].title(), end = ' ')
            for i in range(1, len(t)):
                print(t[i], end = ' ')
            print()
        # print()

    except:
        break

