a, b, c = map(int, input().split())
d = int(input())

c += d
b += c//60
a += b//60
a = a%24
b = b%60
c = c%60
print(a, b, c)