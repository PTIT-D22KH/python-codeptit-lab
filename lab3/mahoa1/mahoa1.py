for _ in range(int(input())):
    s = input()
    curr = s[0]
    count = 1
    res = ""
    for i in range(1, len(s)):
        if s[i] != curr:
            res += f"{count}{curr}"
            count = 1
        else:
            count += 1
        curr = s[i]
    if (count >= 1):
        res += f"{count}{curr}"
    print(res)