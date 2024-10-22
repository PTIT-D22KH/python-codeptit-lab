class Course:
    def __init__(self, id, name, testType):
        self.id = id
        self.name = name
        self.testType = testType    
    def __str__(self):
        return f"{self.id} {self.name} {self.testType}"

def cmp(a):
    return (a.id)

def solve():
    n = int(input())
    a = []
    for i in range(n):
        a.append(Course(input(), input(), input()))
    a.sort(key = cmp)
    for x in a:
        print(str(x))

solve()