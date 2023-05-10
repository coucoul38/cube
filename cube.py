from math import *
#############################
# --> pip install sympy <-- #
#############################
from sympy import *
# sympy remplace les valeurs numériques des racinnes carrèes par sqrt() --> + simple à lire et exact

def cube(x,y,z):
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
    
    P = [[-2/sqrt(6), -1/sqrt(6), 1/sqrt(6)], [0, 1/sqrt(2), 1/sqrt(2)], [-sqrt(3)/3, sqrt(3)/3, -sqrt(3)/3]]

    for index in points:
        newVect = [index[0]*P[0][0]+index[1]*P[0][1]+index[2]*P[0][2],index[0]*P[1][0]+index[1]*P[1][1]+index[2]*P[1][2], index[0]*P[2][0]+index[1]*P[2][1]+index[2]*P[2][2]]
        newPoints[points.index(index)] = newVect;

    for i in range(8):
       print(newPoints[i])

cube(0,0,0)