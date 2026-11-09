def maksimal(a, b):
    if a > b:
        return a
    return b

def minimal(a, b):
    if a < b:
        return a
    return b

n = int(input())
angka = list(map(int, input().split()))

maks = angka[0]
minim = angka[0]

for nilai in angka:
    maks = maksimal(maks, nilai)
    minim = minimal(minim, nilai)

print(maks, minim)
