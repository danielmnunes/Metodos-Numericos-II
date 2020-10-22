'''
Curso: Métodos Numéricos II
Professor: Creto Augusto Vidal
Semestre: 2020.1
Equipe: DANIEL MAGALHÃES NUNES, ANTONIO AUGUSTO DA SILVA HOLANDA
Tarefa 08
'''
# Área de superfícies 2D
import numpy as np
n=30
x = np.polynomial.legendre.leggauss(n)[0]
w = np.polynomial.legendre.leggauss(n)[1]

sol = 0
for i in range(n):
    for j in range(n):
        sol += w[i]*w[j]*np.sqrt(
            np.power(16 * x[j] * np.cos(x[i]), 2) +
            np.power(16 * x[j] * np.sin(x[i]), 2) +
            1)

sol *= 1600
print(sol)