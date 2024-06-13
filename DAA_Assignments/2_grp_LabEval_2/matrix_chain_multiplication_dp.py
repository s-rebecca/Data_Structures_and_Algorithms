import sys

def matrix_chain_order(p):
    n = len(p) - 1  # number of matrices

    # m[i][j] will store the minimum number of scalar multiplications needed to compute the matrix A[i]A[i+1]...A[j]
    # s[i][j] will store the split index that leads to the optimal parenthesization
    m = [[0 for _ in range(n)] for _ in range(n)]
    s = [[0 for _ in range(n)] for _ in range(n)]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            m[i][j] = sys.maxsize

            for k in range(i, j):
                # Calculate the number of scalar multiplications
                cost = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]

                # Update if we found a better cost
                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k

    return m, s

def print_parenthesis(s, i, j):
    if i == j:
        print(f"A{i+1}", end="")
    else:
        print("(", end="")
        print_parenthesis(s, i, s[i][j])
        print_parenthesis(s, s[i][j] + 1, j)
        print(")", end="")

# Example of how to use the functions
matrix_dimensions = [30, 35, 15, 5, 10, 20, 25]  # Dimensions of matrices A1, A2, ..., An
m, s = matrix_chain_order(matrix_dimensions)
print("Minimum number of multiplications:", m[0][len(matrix_dimensions) - 2])
print("Optimal Parenthesization: ", end="")
print_parenthesis(s, 0, len(matrix_dimensions) - 2)
