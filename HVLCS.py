def hvlcs(A, B, val):
    m, n = len(A), len(B)
    M = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if A[i-1] == B[j-1]:
                M[i][j] = val[A[i-1]] + M[i-1][j-1]
            else:
                M[i][j] = max(M[i-1][j], M[i][j-1])
    return M

def backtrack(M, A, B):
    seq, i, j = [], len(A), len(B)
    while i > 0 and j > 0:
        if A[i-1] == B[j-1]:
            seq.append(A[i-1])
            i -= 1; j -= 1
        elif M[i-1][j] >= M[i][j-1]:
            i -= 1
        else:
            j -= 1
    return ''.join(reversed(seq))

val = {'e': 2, 'r': 4, 'g': 6}
A, B = "gree", "reger"
M = hvlcs(A, B, val)
print(M[len(A)][len(B)])
print(backtrack(M, A, B))