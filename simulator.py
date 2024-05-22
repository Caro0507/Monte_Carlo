#!/usr/bin/env python3

from sys import argv
from random import uniform



def _points_(nb_pixels):
    facteur_x=nb_pixels/2
    compt=0
    couleur=2
    x,y=uniform(-1,1),uniform(-1,1)
    if x**2+y**2 <= 1:
        compt=1
        couleur=1
    return [compt,[int(facteur_x*(x+1)), int(facteur_x*(y+1)), couleur]]

if __name__== '__main__':
    if len(argv)!=2 or not(str.isdigit(argv[1])) or int(argv[1])==0 :
        print ("\n\n    ERREUR\n")
        print("Veuillez entrer une ligne de commande de la forme : \n" )
        print("    python3 " + argv[0] + " n \navec n un entier strictement positif\n\n")
    else:
        n=int(argv[1])
        COMPT_PTS =0
        for i in range(n):
            COMPT_PTS+=_points_(0)[0]
        print (4*COMPT_PTS/n)
