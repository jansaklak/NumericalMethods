import numpy as np
A = np.array(
    [[( 19/12),( 13/12),( 5/6),( 5/6),( 13/12),(-17/12)],
     [( 13/12),( 13/12),( 5/6),( 5/6),(-11/12),( 13/12)],
     [(  5/6 ),(  5/6 ),( 5/6),(-1/6),(  5/6 ),(  5/6 )],
     [(  5/6 ),(  5/6 ),(-1/6),( 5/6),(  5/6 ),(  5/6 )],
     [( 13/12),(-11/12),( 5/6),( 5/6),( 13/12),( 13/12)],
     [(-17/12),( 13/12),( 5/6),( 5/6),( 13/12),( 19/12)]])

def HouseHolder(A):
    print(A)
    n = A.shape[0]
    U = np.eye(n)
    for i in range(n-2):
        x = A[i+1:, i]
        e1 = np.zeros_like(x)
        e1[0] = np.linalg.norm(x)
        u = x - e1
        v = u / np.linalg.norm(u)
        Q = np.eye(n)
        Q[i+1:, i+1:] -= 2 * np.outer(v, v)
        A = np.dot(Q, A)
        U = np.dot(U, Q)
    return U

def DoTrojdiagonalnej(ma):
    A = ma
    P = HouseHolder(A)
    P1A = np.dot(P,A)
    P1T = np.transpose(P)
    A = np.dot(P1A,P1T)
    for i in range (2,A.shape[0]-2):
        P = HouseHolder(A[i:,i:])
        P1A = np.dot(P,A[i:,i:])
        P1T = np.transpose(P)
        A = np.dot(P1A,P1T)
    return A
        
Ah = HouseHolder(A)
AhOdw = np.linalg.inv(Ah)
jeden = np.dot(Ah,AhOdw)
print(DoTrojdiagonalnej(A))
