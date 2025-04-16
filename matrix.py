A = [
    [1,2,3,4,5],
    [2,3,4,5,6],
    [9,3,5,6,7],
    [8,5,6,3,2],
    [9,4,6,8,9],
]

B = [
    [1,2,3,4,9],
    [2,3,6,9,6],
    [9,3,9,6,7],
    [8,5,5,3,2],
    [9,6,6,8,9],
]

hasil = [
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]
]

for i in range(5):
    for j in range(5):
        for k in range(5):
         hasil[i][j] += A[i][k] * B[k][j]
         
print("Matrix A: ")
for baris in A:
   print(baris)

print("Matriks B: ")
for baris in B:
   print(baris)


print("hasil:")
for baris in hasil:
    print(baris)