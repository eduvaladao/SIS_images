# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import matplotlib.colors 

cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", ["black","rebeccapurple","white"])


print ("*-----------------------------------------------------------------------------------------*")
print ("| SIS Surface Brightness Simulator for spiral and elliptical galaxies (elliptical source) |")
print ("*-----------------------------------------------------------------------------------------*")

print ("Insira os valores para o centro da fonte de coordenadas cartesianas S1 e S2:")
S1 = float(input("S1 = "))
S2 = float(input("S2 = ")) 

print ("Insira o valor para a excentricidade da sua fonte elíptica entre 0 e 1, sendo 1 não incluído:")
e = float(input("e = ")) 

print ("Insira o ângulo (em graus) desejado do eixo-maior da elipse em relação ao eixo x1 cartesiano no sentido anti-horário:")
phie = float(input("phie = "))*(np.pi/180)

print ("Escolha o valor de n entre 1 e 10 da lei de Sérsic para simular o perfil de brilho do bojo de uma galáxia espiral (dica: a lei de de Vaucouleurs, n = 4, é uma ótima opção):")
n = float(input("n = ")) 

print ("Escolha os valores para o bojo de Re (raio efetivo que contém metade da luminosidade total da galáxia) e Ie (brilho superficial isofota efetivo correspondente a Re) e para o disco escolha Io (brilho superficial central extrapolado) e Ro (distância entre o centro e o ponto do disco onde o brilho decai por um fator 1/e):")
S = float(input("Ie = "))
Rs = float(input("Re = "))
B = float(input("Io = "))
Rb = float(input("Ro = "))

def f(x1,x2):
    return S*10**(-(0.868*n-0.142)*(((np.sqrt((1-e)*((x2*np.sin(phie)+x1*np.cos(phie))*(1-(1/np.sqrt(x1**2+x2**2)))-S1*np.cos(phie)-S2*np.sin(phie))**2 + (1+e)*((x2*np.cos(phie)-x1*np.sin(phie))*(1-(1/np.sqrt(x1**2+x2**2)))+S1*np.sin(phie)-S2*np.cos(phie))**2))/Rs)**(1/n)-1)) + B*np.exp(-((np.sqrt((1-e)*((x2*np.sin(phie)+x1*np.cos(phie))*(1-(1/np.sqrt(x1**2+x2**2)))-S1*np.cos(phie)-S2*np.sin(phie))**2 + (1+e)*((x2*np.cos(phie)-x1*np.sin(phie))*(1-(1/np.sqrt(x1**2+x2**2)))+S1*np.sin(phie)-S2*np.cos(phie))**2))/Rb))

x1 = np.linspace(-2, 2, 1000)
x2 = np.linspace(-2, 2, 1000)

X1, X2 = np.meshgrid(x1, x2)
R = f(X1,X2)

plt.figure(1)
plt.contourf(X1, X2, R, 50, cmap='RdGy')
plt.ylabel('$x_2$')
plt.xlabel('$x_1$')
#plt.ylim(-1,1)
#plt.xlim(-1,1)
plt.colorbar()

print ("Insira o valor para R0:")
r0 = float(input("R0 = ")) 
level = [S*10**(-(0.868*n-0.142)*((r0/Rs)**(1/n)-1)) + B*np.exp(-r0/Rb)]
print('I(R0)', level)

plt.figure(2)
#contours = plt.contour(X1, X2, R, level, colors='blue')
#plt.clabel(contours, levels, fontsize=8) 
plt.imshow(R, extent=[-2, 2, -2, 2], vmin=S*10**(-(0.868*n-0.142)*((r0/Rs)**(1/n)-1)) + B*np.exp(-r0/Rb), origin='lower', cmap='RdGy', alpha=1.0)
plt.ylabel('$x_2$', fontsize=12)
plt.xlabel('$x_1$', fontsize=12)
plt.colorbar(label='I($x_1$,$x_2$)')
plt.tick_params(labelsize='small') 
plt.savefig('lsg1.pdf', dpi=1000)

plt.figure(3)
plt.imshow(R, extent=[-2, 2, -2, 2], vmin=S*10**(-(0.868*n-0.142)*((r0/Rs)**(1/n)-1)) + B*np.exp(-r0/Rb), origin='lower', cmap=cmap, alpha=1.0)
plt.ylabel('$x_2$', fontsize=12)
plt.xlabel('$x_1$', fontsize=12)
plt.colorbar(label='I($x_1$,$x_2$)')
plt.tick_params(labelsize='small')
plt.savefig('lsg2.pdf', dpi=1000)

plt.figure(4)
plt.imshow(R, extent=[-2, 2, -2, 2], vmin=S*10**(-(0.868*n-0.142)*((r0/Rs)**(1/n)-1)) + B*np.exp(-r0/Rb), origin='lower', cmap='gist_gray', alpha=1.0)
plt.ylabel('$x_2$', fontsize=12)
plt.xlabel('$x_1$', fontsize=12)
plt.colorbar(label='I($x_1$,$x_2$)')
plt.tick_params(labelsize='small')
plt.savefig('lsg3.pdf', dpi=1000)

plt.figure(5)
ax = plt.axes(projection='3d')
ax.contour3D(X1, X2, R, 50, cmap='RdGy')
ax.set_ylabel('$x_2$')
ax.set_xlabel('$x_1$')
ax.set_zlabel('I($R_0$)')


plt.show()  
