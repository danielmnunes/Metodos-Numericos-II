'''
Curso: Métodos Numéricos II
Professor: Creto Augusto Vidal
Semestre: 2020.1
Equipe: DANIEL MAGALHÃES NUNES, ANTONIO AUGUSTO DA SILVA HOLANDA
Tarefa 07
'''

import numpy as np

def g(valor):
    return np.divide(1, np.power(valor, 1/2))

def x_de_s(valor):
    global a, b
    v1 = np.divide(a+b, 2)
    v2 = np.divide(b-a, 2)*np.tanh(valor)

    return v1 + v2

def dx_de_s(valor):
    global a, b
    v1 = np.divide(b-a, 2)
    v2 = np.divide(1,np.power(np.cosh(valor), 2))
    return v1 * v2

def f(valor):
    global a, b
    return g(x_de_s(valor))*dx_de_s(valor)

def simpson38_fechada(f, n, c):
    global a, b
    h = (2*c)/n
    sol = 0
    x = np.linspace(-c, c, n+1)
    for i in range(n):
        sol += f(x[i]) + 3*f(x[i] + (h/3)) + 3*f(x[i] + (2*h/3)) +  f(x[i] + h)
    sol *= h/8
    return sol

a = 0
b = 1
c = 6
n = 100
sol = simpson38_fechada(f,n, c)
print(sol)
# 1.9950