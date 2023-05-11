from math import *
#############################
# --> pip install sympy <-- #
#############################
from sympy import *
# sympy remplace les valeurs numériques des racinnes carrèes par sqrt() --> + simple à lire et exact

def reflet(x,y,z): #(x,y,z) sont les coordonées du point a du cube
    roundTo = 2
    #coordonnées des points du cube dans le repère (O,i,j,k):
    a = (x,y,z)
    b = (1+x,y,z)
    c = (1+x,y,z)
    d = (x,y,1+z)
    e = (x,1+y,z)
    f = (1+x,1+y,z)
    g = (1+x,1+y,1+z)
    h = (x,1+y,1+z)
    points = [a,b,c,d,e,f,g,h]
    newPoints = points

    for index in points:
        x = index[0]
        y = index[1]
        z = index[2]
        newVect = [round(8*x/9 - 4*y/9 - 4*z/9, roundTo), round(-4*x/9 + 5*y/9 - 8*z/9, roundTo), round(-4*x/9 - 8*y/9 + 5*z/9, roundTo)]
        newPoints[points.index(index)] = newVect

    print("Coordonées des 8 points (dans l'ordre de a à h):")
    for i in range(8):
       print(i+1,"->",newPoints[i])

reflet(0,0,0) #remplacer par les (x,y,z) que vous voulez