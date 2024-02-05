import numpy as np
A = np.array(
    [[( 19/12),( 13/12),( 5/6),( 5/6),( 13/12),(-17/12)],
     [( 13/12),( 13/12),( 5/6),( 5/6),(-11/12),( 13/12)],
     [(  5/6 ),(  5/6 ),( 5/6),(-1/6),(  5/6 ),(  5/6 )],
     [(  5/6 ),(  5/6 ),(-1/6),( 5/6),(  5/6 ),(  5/6 )],
     [( 13/12),(-11/12),( 5/6),( 5/6),( 13/12),( 13/12)],
     [(-17/12),( 13/12),( 5/6),( 5/6),( 13/12),( 19/12)]])

def MetodaPotegowa(A):
    n=100
    prog=pow(10,-4)
    zk = np.random.rand(A.shape[1])
    for i in range(n):
        zk = np.dot(A, zk)
        yk1 = np.linalg.norm(zk)
        zk /= yk1
        if i > 0:
            error = np.abs(yk1 - yk)
            if error < prog:
                break
        yk = yk1
    return yk1

print(MetodaPotegowa(A))
