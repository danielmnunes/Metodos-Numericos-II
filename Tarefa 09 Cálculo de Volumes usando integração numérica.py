'''
Curso: Métodos Numéricos II
Professor: Creto Augusto Vidal
Semestre: 2020.1
Equipe: DANIEL MAGALHÃES NUNES, ANTONIO AUGUSTO DA SILVA HOLANDA
Tarefa 09
'''
# Volume de superfícies 2D exemplo
import numpy as np
n=3
x = np.polynomial.legendre.leggauss(n)[0]
w = np.polynomial.legendre.leggauss(n)[1]

sol = 0
for i in range(n):
    for j in range(n):
        sol += w[i]*w[j]*(np.power(40 * x[j], 2) - np.power(20 * x[i], 2))

sol *= 160
print(sol)


# ---------------------------------------------
# Volume da elipse

n=3
x = np.polynomial.legendre.leggauss(n)[0]
w = np.polynomial.legendre.leggauss(n)[1]

sol = 0
for i in range(n):
    for j in range(n):
        sol += w[i] * w[j] * (np.power(16 * x[j] * np.cos(x[i]), 2) - np.power(16 * x[j] * np.sin(x[i]),2))

sol *= 1600
print(sol)