def strassen_multiply(A, B):
    if len(A) != 2 or len(A[0]) != 2 or len(B) != 2 or len(B[0]) != 2:
        raise ValueError("Input matrices must be 2x2")

    # Matrix dimensions
    a11, a12, a21, a22 = A[0][0], A[0][1], A[1][0], A[1][1]
    b11, b12, b21, b22 = B[0][0], B[0][1], B[1][0], B[1][1]

    # Calculate intermediate values
    M1 = (a11 + a22) * (b11 + b22)
    M2 = (a21 + a22) * b11
    M3 = a11 * (b12 - b22)
    M4 = a22 * (b21 - b11)
    M5 = (a11 + a12) * b22
    M6 = (a21 - a11) * (b11 + b12)
    M7 = (a12 - a22) * (b21 + b22)

    # Calculate the resulting matrix C
    C = [[0, 0], [0, 0]]
    C[0][0] = M1 + M4 - M5 + M7
    C[0][1] = M3 + M5
    C[1][0] = M2 + M4
    C[1][1] = M1 - M2 + M3 + M6

    return C

# Example usage
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

result = strassen_multiply(A, B)
for row in result:
    print(row)