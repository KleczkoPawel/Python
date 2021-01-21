import math
import matplotlib.pyplot as plt
import numpy as np
def rzut(v0,alfa):
    zasieg = v0*v0*math.sin(2*alfa*3.14/180)/9.81
    Hmax = v0*v0*math.sin(alfa*3.14/180)*math.sin(alfa*3.14/180)/2*9.81*0.01
    tc = 2*v0*math.sin(alfa*3.14/180)/9.81
    t = np.linspace(0,tc,100)
    vy = v0*math.sin(alfa*3.14/180)-9.81*t
    vx = v0*math.cos(alfa*3.14/180)
    x = vx*t
    y = vy*t-(9.81/2)*t*t
    tor = x*math.tan(alfa*3.14/180)-((9.81*x*x)/2*v0*v0*math.cos(alfa*3.14/180)*math.cos(alfa*3.14/180))
    print('zasieg = ',zasieg,'\nwysokosc maksymalna = ',Hmax,'\ncałkowity czas = ',tc)
    
    plt.figure()
    plt.subplot(3,1,1)
    plt.plot(t,vy)
    plt.title('predkosc vy po czasie t')
    plt.xlabel('czas [s]')
    plt.ylabel('vy')

    plt.subplot(3,1,2)
    plt.plot(t,y,t,x)
    plt.title('Położenie')
    plt.xlabel('czas [s]')
    plt.ylabel('x , y')

    plt.subplot(3,1,3)
    plt.plot(x,tor)
    plt.title('tor rzutu')
    plt.xlabel('x')
    plt.ylabel('y')

    plt.show()
rzut(15,45)