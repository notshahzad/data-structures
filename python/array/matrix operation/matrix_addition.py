m_a = [[3,4],[6,7]]
m_b = [[6,1],[-1,-2]]
def squarematrixadd(a,b):
    length = len(a)
    c = [[None]*length,[None]*length]
    for i in range(length):
        for j in range(length):
            c[i][j] = a[i][j]+b[i][j]
    return c
print(squarematrixadd(m_a,m_b))