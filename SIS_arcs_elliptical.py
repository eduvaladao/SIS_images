import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
np.seterr(divide='ignore', invalid='ignore')

mpl.rcParams['mathtext.fontset'] = 'cm'
#mpl.rcParams['font.family'] = 'STIXGeneral'

# Image formation - SIS with circular source

phi = np.arange(0.0, 2.0*np.pi, 0.0001)
xc1=np.cos(phi) #curva critica para eixo x1
xc2=np.sin(phi) #curva critica para eixo x2

def xmenos(r0, s, theta, e, phie):
    return np.where(1+(1/(1-e*np.cos(2*(phi-phie))))*(s*np.cos(theta-phi)-e*s*np.cos(theta+phi-2*phie)-np.sqrt((r0**2)*(1-e*np.cos(2*(phi-phie)))-(s**2)*(1-e**2)*np.sin(theta-phi)**2))<0,np.nan,\
      1+(1/(1-e*np.cos(2*(phi-phie))))*(s*np.cos(theta-phi)-e*s*np.cos(theta+phi-2*phie)-np.sqrt((r0**2)*(1-e*np.cos(2*(phi-phie)))-(s**2)*(1-e**2)*np.sin(theta-phi)**2)))

def xmais(r0, s, theta, e, phie):
    return np.where(1+(1/(1-e*np.cos(2*(phi-phie))))*(s*np.cos(theta-phi)-e*s*np.cos(theta+phi-2*phie)+np.sqrt((r0**2)*(1-e*np.cos(2*(phi-phie)))-(s**2)*(1-e**2)*np.sin(theta-phi)**2))<0,np.nan,\
      1+(1/(1-e*np.cos(2*(phi-phie))))*(s*np.cos(theta-phi)-e*s*np.cos(theta+phi-2*phie)+np.sqrt((r0**2)*(1-e*np.cos(2*(phi-phie)))-(s**2)*(1-e**2)*np.sin(theta-phi)**2)))


r0 = float(input("R0 = "))
s = float(input("S = "))
theta = float(input("theta = "))*(np.pi/180)
e = float(input("e = "))
phie = float(input("phie = "))*(np.pi/180) 
    

#subplot(nrows,nlines,position)

#====================================================================================================
# Source Sketch - Source Plane
#====================================================================================================

ax1 = plt.subplot(121)
plt.plot(np.cos(phi), np.sin(phi),'k--',0,0,'ko')
plt.plot(s*np.cos(theta)+(r0/(np.sqrt(1-e)))*np.cos(phi)*np.cos(phie)-(r0/(np.sqrt(1+e)))*np.sin(phi)*np.sin(phie),s*np.sin(theta)+(r0/(np.sqrt(1-e)))*np.cos(phi)*np.sin(phie)+(r0/(np.sqrt(1+e)))*np.sin(phi)*np.cos(phie),'purple')
titlefont = {
        'family' : 'serif',
        'color'  : 'black',
  #      'weight' : 'bold',
        'size'   : 16,
        }

ax1.set_title("Plano das Fontes", # title
             va='bottom',                   # some space below the title
             fontdict = titlefont           # set the font properties
             )        
ax1.grid(False, which='both')
ax1.axis([-2,2, -2, 2])
ax1.axhline(y=0, color='0.9',ls='--',lw=1)
ax1.axvline(x=0, color='0.9',ls='--',lw=1)
ax1.set_aspect('equal', adjustable='box')
plt.xlabel(r'$y_{1}$',fontsize=20)
plt.ylabel(r'$y_{2}$',fontsize=20)

#====================================================================================================
# Image Formation - Lens Plane
#====================================================================================================


ax2 = plt.subplot(122)
plt.plot(xc1, xc2, 'k--', lw=1, label=r'$x_c$')
plt.plot(xmenos(r0, s, theta, e, phie)*np.cos(phi), xmenos(r0, s, theta, e, phie)*np.sin(phi), 'b-', lw=1.3, label=r'$x^{-}$')
plt.plot(xmais(r0, s, theta, e, phie)*np.cos(phi), xmais(r0, s, theta, e, phie)*np.sin(phi), 'r-', lw = 1.3, label=r'$x^{+}$') 
plt.plot((1+(1/(1-e*np.cos(2*(phi-phie))))*(s*np.cos(theta-phi)-e*s*np.cos(theta+phi-2*phie)))*np.cos(phi), (1+(1/(1-e*np.cos(2*(phi-phie))))*(s*np.cos(theta-phi)-e*s*np.cos(theta+phi-2*phie)))*np.sin(phi) ,  'k--', lw=0.5, label=r'$\bar{x}$')
titlefont = {
        'family' : 'serif',
        'color'  : 'black',
  #      'weight' : 'bold',
        'size'   : 16,
        }

ax2.set_title("Plano das Lentes", # title
             va='bottom',                   # some space below the title
             fontdict = titlefont           # set the font properties
             )        
ax2.grid(False, which='both')
ax2.axis([-2,2, -2, 2])
ax2.axhline(y=0, color='0.9',ls='--',lw=1)
ax2.axvline(x=0, color='0.9',ls='--',lw=1)
ax2.set_aspect('equal', adjustable='box')
plt.xlabel(r'$x_{1}$',fontsize=20)
plt.ylabel(r'$x_{2}$',fontsize=20)

ax2.legend(loc="lower left")           # legend location

plt.show() 

