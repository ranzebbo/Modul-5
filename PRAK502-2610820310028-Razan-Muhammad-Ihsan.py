def hitung(nilai1, nilai2):
    return nilai1 - nilai2

def mutlak(angka):
    return abs(angka)

data = input().split()


if len(data) == 1 and len(data[0]) == 4 and data[0].isdigit():
    x1, y1, x2, y2 = map(int, data[0])
else:
    x1, y1, x2, y2 = map(int, data)

hasil = mutlak(hitung(x1, x2)) + mutlak(hitung(y1, y2))
print(hasil)
