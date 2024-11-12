s = input()
countLower = 0
countUpper = 0
for c in s:
    if (ord(c) >= ord('a') and ord(c) <= ord('z')):
        countLower += 1
    elif(ord(c) >= ord('A') and ord(c) <= ord('Z')):
        countUpper += 1
if (countLower >= countUpper):
    print(s.lower())
else:
    print(s.upper())