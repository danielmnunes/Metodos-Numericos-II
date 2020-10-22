# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 12:36:31 2020

Equipe: DANIEL MAGALHÃES NUNES
        ANTONIO AUGUSTO DA SILVA HOLANDA
"""
import numpy as np



def trapezio_fechada(f, a , b, n):
    h = (b-a)/n
    sol = 0
    x = np.linspace(a, b, n+1)
    y = f(x)
    for i in range(n):
        sol += y[i] + y[i+1]
    sol *= h/2
    return sol

def trapezio_aberta(f, a , b, n):
    h = (b-a)/n
    sol = 0
    x = np.linspace(a, b, n+1)
    for i in range(n):
        sol += f(x[i] + h/3) + f(x[i] + (2/3)*h)  
    sol *= h/2
    return sol

def simpson13_fechada(f, a , b, n):
    h = (b-a)/n
    sol = 0
    x = np.linspace(a, b, n+1)
    for i in range(n):
        sol += f(x[i]) + 4*f(x[i] + (h/2)) + f(x[i] + h)
    sol *= h/6
    return sol
    
def simpson13_aberta(f, a , b, n):
    h = (b-a)/n
    sol = 0
    x = np.linspace(a, b, n+1)
    for i in range(n):
        sol += 2*f(x[i] + (1/4)*h) - f(x[i] + (1/2)*h) + 2*f(x[i] + (3/4)*h)  
    sol *= h/3
    return sol

def simpson38_fechada(f, a , b, n):
    h = (b-a)/n
    sol = 0
    x = np.linspace(a, b, n+1)
    for i in range(n):
        sol += f(x[i]) + 3*f(x[i] + (h/3)) + 3*f(x[i] + (2*h/3)) +  f(x[i] + h)
    sol *= h/8
    return sol
    
def simpson38_aberta(f, a , b, n):
    h = (b-a)/n
    sol = 0
    x = np.linspace(a, b, n+1)
    for i in range(n):
        sol += (f(x[i] + (1/5)*h)*11 +
                f(x[i] + (2/5)*h) +
                f(x[i] + (3/5)*h) +
                f(x[i] + (4/5)*h)*11)
    sol *= h/24
    return sol
    
def boole_fechada(f, a , b, n):
    h = (b-a)/n
    sol = 0
    x = np.linspace(a, b, n+1)
    for i in range(n):
        sol += (7*f(x[i])+
                32*f(x[i] + (1/4)*h) +
                12*f(x[i] + (2/4)*h) +
                32*f(x[i] + (3/4)*h) +
                7*f(x[i] + h))
    sol *= h/90
    return sol
    

def boole_aberta(f, a , b, n):
    h = (b-a)/n
    sol = 0
    x = np.linspace(a, b, n+1)
    for i in range(n):
        sol += (11*f(x[i] + (1/6)*h) -
                14*f(x[i] + (2/6)*h) +
                26*f(x[i] + (3/6)*h) -
                14*f(x[i] + (4/6)*h) +
                11*f(x[i] + (5/6)*h))
    sol *= h/20
    return sol






def teste(f, a , b, tol, metodo, sol):
    if metodo == 1:
        integral = trapezio_fechada
    elif metodo == 2:
        integral = trapezio_aberta
    elif metodo == 3:
        integral = simpson13_fechada
    elif metodo == 4:
        integral = simpson13_aberta
    elif metodo == 5:
        integral = simpson38_fechada
    elif metodo == 6:
        integral = simpson38_aberta
    elif metodo == 7:
        integral = boole_fechada
    elif metodo == 8:
        integral = boole_aberta
    
    
    
    n=1
    valor = integral(f, a, b, n)
    
    while np.abs(valor - sol) > tol:
        n +=1
        valor = integral(f, a, b, n)
    
    return n
        
def f(x):
    return np.e**x

sol = np.e - 1
a = 0
b = 1
tol = 1e-6

resultados = []

for i in range(1, 9):
    resultados.append(teste(f, a, b, tol, i, sol))

print(resultados)
# [379, 219, 5, 5, 5, 5, 1, 2]
    
    


