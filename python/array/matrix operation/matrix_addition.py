m_a = [[3,4],[6,7]]
m_b = [[6,1],[-1,-2]]
def matrixadd(a,b):
    length = len(a)
    c = [[None]*length,[None]*length]
    for i in range(length):
        for j in range(length):
            c[i][j] = a[i][j]+b[i][j]
    return c
print(matrixadd(m_a,m_b))