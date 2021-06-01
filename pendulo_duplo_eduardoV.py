"""
Simulação de um pêndulo duplo

Autor: Eduardo da Costa Valadão - eduardovaladao98@gmail.com
"""

import matplotlib.pyplot as plt
from runge_kutta_eduardoV import * 

print ("*---------------------------------------------------------------------------*")
print ("| Simulação de um pêndulo duplo utilizando-se o método de Runge-Kutta (RK4) |")
print ("*---------------------------------------------------------------------------*")

a = float(input('Insira o comprimento da haste ligado a massa 1: '))
b = float(input('Insira o valor da massa 1: '))
c = float(input('Insira o comprimento da segunda haste: '))
d = float(input('Insira o valor da massa 2: '))
t0 = float(input('Escolha um tempo inicial: '))
tf = float(input('Escolha um tempo final: '))
x = float(input('Escolha o intervalo entre cada item da lista de tempo: '))
gr = float(input('Escolha a gravidade local g: '))

print ("*-----------------------*")
print ("| Condições de contorno |")
print ("*-----------------------*")

theta1_0 = float(input('Insira o valor de theta1 em t = 0: '))
alfa1_0 = float(input('Insira o valor da derivada de theta1 em t = 0: '))
theta2_0 = float(input('Insira o valor de theta2 em t = 0: '))
alfa2_0 = float(input('Insira o valor da derivada de theta2 em t = 0: '))


def theta1_prime(t, theta1, theta2, alfa1, alfa2):
    return alfa1

def theta2_prime(t, theta1, theta2, alfa1, alfa2):
    return alfa2

def alfa1_prime(t, theta1, theta2, alfa1, alfa2, l1 = a, l2 = c, m1 = b, m2 = d, g = gr):
    return (m2*(g*np.cos(theta1 - theta2)*np.sin(theta2) - np.sin(theta1 - theta2)*(l1*(alfa1**2)*np.cos(theta1 - theta2) + l2*(alfa2**2))) - (m1 + m2)*g*np.sin(theta1))/(l1*((m1 + m2) - m2*(np.cos(theta1 - theta2)**2)))

def alfa2_prime(t, theta1, theta2, alfa1, alfa2, l1 = a, l2 = c, m1 = b, m2 = d, g = gr):
    return ((m1 + m2)/(l2*((m1 + m2) - m2*(np.cos(theta1 - theta2)**2))))*(g*(np.sin(theta1)*np.cos(theta1 - theta2) - np.sin(theta2)) + l1*(alfa1**2)*np.sin(theta1 - theta2) + (m2*l2*(alfa2**2)*np.sin(theta1 - theta2)*np.cos(theta1 - theta2))/(m1 + m2))

t = np.arange(t0, tf+1, x)
theta1, theta2, alfa1, alfa2 = runge_kutta_4order(theta1_prime, theta2_prime, alfa1_prime, alfa2_prime, t, theta1_0, theta2_0, alfa1_0, alfa2_0)


plt.plot(t, theta1)
plt.xlabel("t (s)")
plt.ylabel("theta1 (radianos)")
plt.show()
plt.plot(t, theta2)
plt.xlabel("t (s)")
plt.ylabel("theta2 (radianos)")
plt.show()
plt.plot(t, alfa1)
plt.xlabel("t (s)")
plt.ylabel("alfa1 (radianos)")
plt.show()
plt.plot(t, alfa2)
plt.xlabel("t (s)")
plt.ylabel("alfa2 (radianos/s)")
plt.show()
plt.plot(theta1, theta2)
plt.xlabel("theta1 (radianos)")
plt.ylabel("theta2 (radianos)")
plt.show()
plt.plot(alfa1, alfa2)
plt.xlabel("alfa1 (radianos)")
plt.ylabel("alfa2 (radianos)")
plt.show()
