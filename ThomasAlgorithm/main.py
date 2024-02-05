import numpy

def StworzMacierz(diag,nad,pod,rozmiar):
	Macierz = numpy.empty([rozmiar,rozmiar])
	for x in range(0,rozmiar):
		for y in range(0,rozmiar):
			if(y == x - 1):
				Macierz[x][y] = nad
			elif(y == x + 1):
				Macierz[x][y] = pod
			elif(x==y):
				Macierz[x][y] = diag
			else:
				Macierz[x][y] = 0
	return Macierz

#Z macierzy tworze liste z 3 kolumnami [][0] - srodkowe elementy [][1] - nad [][2] - pod
def JakoWektory(macierz,dlugosc):
	Wektory = numpy.zeros([dlugosc,3])
	for i in range(0,dlugosc):
		Wektory[i][0] = macierz[i][i]
		if i<dlugosc-1:
			Wektory[i][1] = macierz[i][i+1]
			Wektory[i][2] = macierz[i+1][i]
	return Wektory
    
def Thomas(wek,Wolne):
	nad = wek[:,1]
	pod = wek[:,2]
	srodek = wek[:,0]
	rozmiar = len(Wolne)

	for i in range(1, rozmiar):
		wsp = pod[i-1] / srodek[i-1]
		srodek[i] = srodek[i] - (wsp * nad[i-1])
		Wolne[i] = Wolne[i] - (wsp * Wolne[i-1])

	wynik = numpy.zeros((rozmiar,1))
	wynik[-1] = Wolne[-1] / srodek[-1] #Zaczynam od ostatniego elementu i zapisuje kolejne aż do 0
	
	for i in range(rozmiar-2, -1, -1):
		wynik[i] = (Wolne[i] - nad[i] * wynik[i+1]) / (srodek[i])
	
	return wynik

def Dokladne(A,B):		#Funkcja do sprawdzania dokładnego wyniku poprzez x = A-1 * B
	rozmiar = len(B)
	wynik = numpy.zeros((rozmiar,1))
	Ai = numpy.linalg.inv(A)
	#print(Ai)  Tez zgadza się z Mathematica
	wynik = numpy.matmul(Ai,B) # matmul i dot dają taki sam wynik
	return wynik

def Oblicz():
	A = StworzMacierz(4,1,1,7)
	print(A)
	Aw = JakoWektory(A, 7)
	print(Aw)
	
	Wolne = [1,2,3,4,5,6,7]
	x = Thomas(Aw, Wolne)
	xd = Dokladne(A, Wolne)

	print("Wynik algorytmu Thomasa")	#Taki sam w Mathmematice
	print(x)
	print("Dokladny: ")					#Nie zgadza się z żadnym z Mathematici
	print(xd)

Oblicz()
