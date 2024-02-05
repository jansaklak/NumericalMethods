import numpy
import math

A = numpy.array([243,-486,783,990,558,-28,-72,16])
B = numpy.array([1,1,3,2,-1,-3,-11,-8,-12,-4,-4])

def Pochodna(W):
    W = numpy.flip(W)
    D = numpy.zeros([len(W)-1,1])
    for n in range (0,len(W)-1):
        D[n] = W[n+1] * (n+1)
    return D

def WartoscWielomianu(wpunkcie,wielomian):
    y=0.0
    rozmiar = len(wielomian)
    for i in range(rozmiar):
        y += wielomian[i]*wpunkcie**i
    return y

def Laguerre(P,zi):
    stopien = len(P) - 1
    l = stopien * WartoscWielomianu(zi, P)
    m1 = WartoscWielomianu(zi, Pochodna(P))
    mp1 = stopien - 1
    mp2 = (stopien-1) * WartoscWielomianu(zi, Pochodna(P)) * WartoscWielomianu(zi, Pochodna(P)) 
    mp3 = stopien * WartoscWielomianu(zi, P)*WartoscWielomianu(zi, Pochodna(Pochodna(W)))
    
    mC1 = m1 + math.sqrt(mp1 * mp2-mp3)
    mC2 = m1 - math.sqrt(mp1 * mp2-mp3)
    
    if(abs(mC1)>abs(mC2)):
        m = mC1
    else:
        m = mC2
    
def laguerre(coeffs, r0, tol=1e-6, maxiter=100):
    n = 0
    r = r0
    while n < maxiter:
        p = coeffs[0]
        for i in range(1, len(coeffs)):
            p = p * r + coeffs[i]
        if abs(p) < tol:
            break
        dp = 0
        ddp = 0
        for i in range(1, len(coeffs)-1):
            dp = (i+1) * coeffs[i+1] + dp * r
            ddp = (i+1) * dp + ddp * r
        if abs(ddp) < tol:
            break
        q, rr = numpy.polydiv(coeffs, [1, -r])
        coeffs = q
        r1 = r - p / dp * (1 - rr / p)
        if abs(r1 - r) < tol:
            break
        r = r1
        n += 1
    return r

print(laguerre(A,4))
