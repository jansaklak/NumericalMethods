import numpy
from Zad1 import StworzMacierz,Thomas,JakoWektory

u1 = numpy.array([[1,0,0,0,0,0,1]])
u2 = u1.transpose()
A1 = numpy.dot(u2,u1)
print(A1)
print(u2)

wolne = numpy.array([[1,2,3,4,5,6,7]])
wolne = wolne.transpose()

A2 = StworzMacierz(4,1,1,7)
odj =  [[1,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,1],]
A2 = A2 - odj

A = StworzMacierz(4,1,1,7)
print(A)
Aw = JakoWektory(A, 7)
Aw[0][0] = 3
Aw[6][0] = 3
Wolne = [1,2,3,4,5,6,7]
z = Thomas(Aw, Wolne)
q = Thomas(Aw, u1[0])
z = numpy.array(z)
q = numpy.array(q)
print("z: ",z)
print("q: ",q)

w1 = numpy.dot(u1,z)
print("vT.z: ", w1)
w2 = 1 + numpy.dot(u1[0],q.transpose()[0])
print("1+vT.q ", w2)
w3 = numpy.dot((w1 / w2),q[0])
print("w1/w2.q", w3)
w = z - w3 
print("Wynik", w)





