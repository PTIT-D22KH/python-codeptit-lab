
def solve():
    n = int(input())
    a = [0] * (n + 1)
    for i in range(n - 1):
        u, v = [int(i) for i in input().split()]
        a[u] += 1
        a[v] += 1
    for i in range(1, n + 1):
        if (a[i] != 1 and a[i] != n - 1) :
            print("No")
            return
    print("Yes")
solve()