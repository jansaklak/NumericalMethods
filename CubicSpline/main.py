import numpy as np
import matplotlib.pyplot as plt
from array import * 

def WartoscFunkcji(x):
    return 1/(1+(5*x*x))

punkty = [(-7/8),(-5/8),(-3/8),(-1/8),(1/8),(3/8),(5/8),(7/8)]

def LiczWartosci(x):
    rozmiar = len(x)
    val = np.empty(rozmiar)
    for i in range (rozmiar):
        val[i] = WartoscFunkcji(x[i])
    return val

def WzorLagrange(x,y,wpunkcie):
    n = len(x)
    interp_val = 0
    for i in range(n):
        mnoz = y[i]
        for j in range(n):
            if j != i:
                mnoz *= (wpunkcie - x[j]) / (x[i] - x[j])
        interp_val += mnoz
    return interp_val

def Roznica(i,y,h):
    wyrazenie = 6 * ((y[i+1] - y[i]) / h[i] - (y[i] - y[i-1]) / h[i-1])
    wyrazenie = wyrazenie / (h[i] + h[i-1])
    return wyrazenie

def RoznicaB(i,A,y,h):
    (y[i+1] - y[i]) / h[i] - h[i] * (2 * A[i] + A[i-1]) / 6

def SplajnKubiczny(wezly,wartosci):
    rozmiar = len(wezly)
    h = np.empty(n-1)
    
    A = np.empty(n)
    A[0] = 0
    A[n-1] = 0
    for i in range(1,rozmiar-1):
        A[i] = Roznica(i,wartosci,h)

def cubic_spline(x, y, x_new):

    n = len(x)
    dx = np.zeros(n-1)
    dy = np.zeros(n-1)
    for i in range (0,n-1):
        dx[i] = x[i+1] - x[i-1]
        dy[i] = y[i+1] - y[i-1]
    A = np.zeros((n, n))
    B = np.zeros(n)
    A[0, 0] = 1
    A[-1, -1] = 1
    for i in range(1, n-1):
        A[i, i-1:i+2] = [dx[i-1], 2*(dx[i-1] + dx[i]), dx[i]]
        B[i] = 3*(dy[i]/dx[i] - dy[i-1]/dx[i-1])
    ddx = np.linalg.solve(A, B)

    a = y
    b = (y[1:] - y[:-1])/dx - dx*(ddx[1:] + 2*ddx[:-1])/3
    c = ddx[:-1]
    d = (ddx[1:] - ddx[:-1])/(3*dx)

    y_new = np.zeros(len(x_new))
    for i in range(n-1):
        t = (x_new - x[i])/(x[i+1] - x[i])
        y_new = a[i] + b[i]*t + c[i]*t**2 + d[i]*t**3
    return y_new

wartosci = np.empty(len(punkty))
wartosci = LiczWartosci(punkty)
print(wartosci)

x = np.linspace(-2.0, 2.0)
#plt.plot(x,WzorLagrange(punkty, wartosci, x))
#plt.plot(x,WartoscFunkcji(x))
plt.plot(x,cubic_spline(punkty,wartosci,x))
plt.plot(punkty,wartosci,"s")
plt.show()
