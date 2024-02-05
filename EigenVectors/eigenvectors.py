import numpy
mat = numpy.zeros((5,5))
eigVal = 0.38917

mat = numpy.array([ [2 ,-1,0 ,0, 1],
                    [-1,2 ,1 ,0, 0],
                    [0 ,1 ,1 ,1, 0],
                    [0 ,0 ,1 ,2,-1],
                    [1 ,0 ,0 ,-1,2]])

def Resolwenta(ma,r):
    A = ma
    rozmiar = A.shape[1]
    wynik = A - r * numpy.zeros_like(rozmiar)
    wynik = numpy.linalg.inv(wynik)
    return wynik
            
def SzukajWektora(ma,val):
    A = ma
    y1 = numpy.random.rand(A.shape[1])
    y1 /= numpy.linalg.norm(y1)
    yk = y1
    for i in range (20):
        zk = numpy.dot(Resolwenta(A,val),yk)
        yk = zk / numpy.linalg.norm(zk)
        print(yk)
    return yk

A = mat - eigVal * numpy.identity(5)
V = numpy.linalg.svd(A)[2]

print(numpy.linalg.eig(mat))
print("Przez Resolwente: ", SzukajWektora(mat,eigVal))
