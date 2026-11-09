def MaxBilangan(a, b, c, d):
    return max(a, b, c, d)

data = input().split()

if len(data) == 1 and len(data[0]) == 4 and data[0].isdigit():
    a, b, c, d = map(int, data[0])
else:
    a, b, c, d = map(int, data)

hasil = MaxBilangan(a, b, c, d)
print(hasil)
