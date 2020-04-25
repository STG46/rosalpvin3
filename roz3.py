a = input()
b, b1, c, c1 = (int(x) for x in input().split())
print(a[b: b1 + 1])
print(a[c: c1 + 1])
