import numpy as np

'''
Алхам бүрт матриц хэвлэх функц
'''
def print_matrix(mat, step):
    print(f"\nАлхам {step}:")
    print(np.array_str(mat, precision=4, suppress_small=True))
    print()

'''
Баганын тоо 4 мөрийн тоо 3 гэж үзвэл
c11 + c21 + c31 + c41 = x
c12 + c22 + c32 + c42 = y
c13 + c23 + c33 + c43 = z байна
Иймд:
Баганын давталтыг c+1 явуулах ёстой. x y z оруулахын тулд
'''
rows = int(input("Мөрийн тоо: "))
cols = int(input("Баганын тоо: "))

A = np.zeros((rows, cols), dtype=float)

'''
Матрицын элемент оруулна хамгийн сүүлд хариуг оруулна
'''
for i in range(rows):
    for j in range(cols):
        A[i, j] = float(input(f"c{i+1}{j+1} = "))

print("\nЭхний матриц:")
print(A)
print()

step = 0

for i in range(min(rows, cols - 1)):
    pivot_row = i
    while pivot_row < rows and np.abs(A[pivot_row, i]) < 1e-12:
        pivot_row += 1
    if pivot_row == rows:
        continue

    if pivot_row != i:
        A[[i, pivot_row]] = A[[pivot_row, i]]
        step += 1
        print_matrix(A, step)
        
    pivot = A[i, i]
    A[i, :] = A[i, :] / pivot
    step += 1
    print_matrix(A, step)
    
    for j in range(rows):
        if j != i:
            factor = A[j, i]
            A[j, :] = A[j, :] - factor * A[i, :]
            step += 1
            print(f"{j+1} мөрийн  {i+1} дахь багана-ийн коэффициент {factor} утгыг арилгав.")
            print_matrix(A, step)

print(A)

inconsistent = False
for i in range(rows):
    if np.allclose(A[i, :-1], 0) and not np.isclose(A[i, -1], 0):
        inconsistent = True
        break

if inconsistent:
    print("Шийдгүй")
elif sum(1 for i in range(rows) if np.abs(A[i,i]-1)<1e-12) < cols - 1:
    print("Олон шийдтэй.")
    print("Матриц:")
    print(A)
else:
    solution = A[:cols-1, -1]
    print("Ганц шийдтэй:")
    for i, sol in enumerate(solution):
        print(f"x{i+1} = {sol}")


'''
3
4
1
2
3
1
2
5
3
2
3
2
5
3
1x + 2y + 3z = 1
2x + 5y + 3z = 2
3x + 2y + 5z = 3
'''