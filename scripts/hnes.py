import sympy as sp


def sym_matrix_from_template(template):
    """
    return a symbolic matrix from a template
    '*' become symbolic, 5 become 5, etc.
    ex: [['*',5], ['*', '*']] -> [[a11, 5],[a21, a22]]

    Template: List[List] (n x n matrix)
    """
    n = len(template)
    matrix = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if template[i][j] == "*":
                matrix[i].append(sp.Symbol("a{}{}".format(i + 1, j + 1)))
            else:
                matrix[i].append(template[i][j])
    matrix = sp.Matrix(matrix)
    print(matrix)
    return matrix


def sym_matrix_n_by_n(n):
    """
    creates n x n matrix of symbols
    n: int
    """
    matrix = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            matrix[i].append(sp.Symbol("a{}{}".format(i + 1, j + 1)))
    matrix = sp.Matrix(matrix)
    print(matrix)
    return matrix


squares = {n**2: n for n in range(1, 10)}


def rollMatrix(matrix):
    # rows and cols
    r, c = matrix.shape
    # if a column vector with n^2 entries
    # we can roll into n x n matrix
    if r not in squares or c != 1:
        print("ex")
        raise Exception(
            "Matrix cannot be unrolled, make sure matrix \
            is square and has atleast 1 entry"
        )
    # the sqrt of r (# of rows) is n for our n x n matrix output
    n = squares[r]
    # n x n matrix of zeros
    new_matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            # remember when indexing 2d arrays, first num is row, second is col
            # also remember python is zero indexed while matlab is 1 indexed
            new_matrix[i][j] = matrix[i * n + j]

    return sp.Matrix(new_matrix)


def unrollMatrix(matrix):
    # rows and cols
    r, c = matrix.shape
    # if a n x n matrix and
    # we can roll into n x n matrix
    if r != c or r <= 0:
        print("ex")
        raise Exception(
            "Matrix cannot be unrolled, make sure matrix \
            has a square number of entries and 1 column"
        )

    # the sqrt of r (# of rows) is n for our n x n matrix output
    n = r
    # if this looks really confusing its called list comprehension
    # and is super powerful, but can get ugly
    # n x n matrix of zeros

    # this works because in sympy matrices
    # can be indexed by one number
    # i think this shouldnt work but i did not make sympy
    new_matrix = [matrix[i] for i in range(n * n)]

    return sp.Matrix(new_matrix)


if __name__ == "__main__":
    sym_matrix_from_template([["*", 5], ["*", "*"]])
    sym_matrix_n_by_n(3)
    # example!
    print(rollMatrix(sp.Matrix([[0], [1], [2], [3], [4], [5], [6], [7], [8]])))
    # example
    print(unrollMatrix(sp.Matrix([[0, 1, 2], [3, 4, 5], [6, 7, 8]])))
