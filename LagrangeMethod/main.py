import numpy
import matplotlib.pyplot as plt
from array import *

punkty =    [0.062500,0.187500,0.312500,0.437500,0.562500,0.687500      ,0.812500     ,0.937500]
wartosci =  [0.687959,0.073443,-0.517558,-1.077264,-1.600455,-2.080815,-2.507266,-2.860307]

def UtworzMacierzV(x):
    rozmiar = len(x)
    V = numpy.empty((rozmiar,rozmiar))
    for i in range (rozmiar):
        for j in range (rozmiar):
            V[i][j] = pow(x[i],j)
    return V

def UtworzMacierzF(y):
    rozmiar = len(y)
    F = numpy.empty((rozmiar))
    for i in range (rozmiar):
        F[i] = y[i]
    return F

def MnozPrzezWektor(A,V):
    res = numpy.zeros([len(V)])
    for i in range(len(A)):
        for k in range(len(V)):
            suma = res[i] + A[i][k] * V[k]
            res[i] = suma
    return res

def WartoscWielomianu(wpunkcie,wielomian):
    y=0.0
    rozmiar = len(wielomian)
    for i in range(rozmiar):
        y += wielomian[i]*wpunkcie**i
    return y

def WzorLagrange(x,y,wpunkcie):
    n = len(x)
    y_new = 0
    for i in range(n):
        mnoz = y[i]
        for j in range(n):
            if j != i:
                mnoz *= (wpunkcie - x[j]) / (x[i] - x[j])
        y_new += mnoz
    return y_new

A = UtworzMacierzV(punkty)
F = UtworzMacierzF(wartosci)
Ainv = numpy.linalg.inv(A)
Wynik = MnozPrzezWektor(Ainv,F)

print("A: ", A)
print("F: ", F)
print("Wynik: ", Wynik)

x = numpy.linspace(-2.0, 2.0)

print("wartosc dla 0.062500",WartoscWielomianu(0.062500, Wynik))
plt.plot(x,WzorLagrange(punkty, wartosci, x))
plt.plot(x,WartoscWielomianu(x, Wynik) + 1)
plt.plot(punkty,wartosci,"s")

plt.show()
