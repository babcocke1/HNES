from sympy import symbols, Array, tensorproduct, Matrix, init_printing, pprint

# A is a n x n complex matrix
n = 4

# makes a 2d array, in our case:
# a list containing n empty lists

matrix = [[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        matrix[i].append(symbols(f"a{i+1}{j+1}"))
print(matrix)
A = Matrix(matrix)
print(A.shape, A.rank)
pprint(A)
AtA = tensorproduct(A, A)
pprint(AtA)
print(AtA.shape)
e11 = Matrix([[1], [0], [0], [0]])
e12 = Matrix([[0], [1], [0], [0]])
e21 = Matrix([[0], [0], [1], [0]])
e22 = Matrix([[0], [0], [0], [1]])
print("A*e11")
pprint(A * e11)
print("A*e12")
pprint(A * e12)
print("A*e21")
pprint(A * e21)
print("A*e22")
pprint(A * e22)

pprint(tensorproduct(m1, m2))
