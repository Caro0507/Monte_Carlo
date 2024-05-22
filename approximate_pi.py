#! /usr/bin/python3

from sys import argv
from os.path import abspath
import subprocess
from numpy import linspace, ones , reshape, product
import simulator



def _ecriture_(img_nombre,str_n,hauteur, position,coef_img):
    coef_1=20*coef_img
    coef_2=30*coef_img
    coef_3=2*coef_1
    epais_taille=2*coef_img
    if str_n== "0" :
        for ordonne in range (coef_3-2*epais_taille) :
            for epaiss in range(epais_taille):
                img_nombre[hauteur+epaiss-coef_1][position+ordonne]    =0
                img_nombre[hauteur+coef_1+epaiss][position+ordonne] =0
        for absc in range(coef_3+epais_taille):
            for epaiss in range(2*coef_img):
                img_nombre[hauteur+absc-coef_1][position+3*epaiss]   =0
                img_nombre[hauteur+absc-coef_1][position+1+3*epaiss] =0
                img_nombre[hauteur+absc-coef_1][position+2+3*epaiss] =0
                img_nombre[hauteur+absc-coef_1][position+coef_2+3*epaiss] =0
                img_nombre[hauteur+absc-coef_1][position+coef_2+1+3*epaiss] =0
                img_nombre[hauteur+absc-coef_1][position+coef_2+2+3*epaiss] =0

    elif str_n == "1" :
        for absc in range(coef_3+epais_taille):
            for epaiss in range(epais_taille):
                img_nombre[hauteur+absc-coef_1][position+coef_2+3*epaiss] =0
                img_nombre[hauteur+absc-coef_1][position+coef_2+1+3*epaiss] =0
                img_nombre[hauteur+absc-coef_1][position+coef_2+2+3*epaiss] =0

    elif str_n == "2" :
        for ordonne in range (coef_3-2*epais_taille) :
            for epaiss in range(epais_taille):
                img_nombre[hauteur+epaiss-coef_1][position+ordonne]    =0
                img_nombre[hauteur+epaiss][position+ordonne] =0
                img_nombre[hauteur+epaiss+coef_1][position+ordonne] =0
        for absc in range(coef_1+coef_img):
            for epaiss in range(epais_taille):
                img_nombre[hauteur+absc+coef_img][position+3*epaiss]   =0
                img_nombre[hauteur+absc+coef_img][position+1+3*epaiss] =0
                img_nombre[hauteur+absc+coef_img][position+2+3*epaiss] =0
                img_nombre[hauteur+absc+coef_img-coef_1][position+coef_2+3*epaiss] =0
                img_nombre[hauteur+absc+coef_img-coef_1][position+coef_2+1+3*epaiss] =0
                img_nombre[hauteur+absc+coef_img-coef_1][position+coef_2+2+3*epaiss] =0

    elif str_n == "3" :
        for ordonne in range (coef_3-2*epais_taille) :
            for epaiss in range(epais_taille):
                img_nombre[hauteur+epaiss-coef_1][position+ordonne]    =0
                img_nombre[hauteur+epaiss][position+ordonne] =0
                img_nombre[hauteur+epaiss+coef_1][position+ordonne] =0
        for absc in range(coef_3+epais_taille):
            for epaiss in range(epais_taille):
                img_nombre[hauteur+absc-coef_1][position+coef_2+3*epaiss] =0
                img_nombre[hauteur+absc-coef_1][position+coef_2+1+3*epaiss] =0
                img_nombre[hauteur+absc-coef_1][position+coef_2+2+3*epaiss] =0

    elif str_n == "4" :
        for ordonne in range (36*coef_img) :
            for epaiss in range(2*coef_img):
                img_nombre[hauteur+epaiss][position+ordonne] = 0
        for absc in range(coef_3+epais_taille):
            for epaiss in range(2*coef_img):
                img_nombre[hauteur-coef_1+absc][position+coef_2+3*epaiss] =0
                img_nombre[hauteur-coef_1+absc][position+coef_2+1+3*epaiss] =0
                img_nombre[hauteur-coef_1+absc][position+coef_2+2+3*epaiss] =0
        for absc in range(21*coef_img):
            for epaiss in range(2*coef_img):
                img_nombre[hauteur-coef_1+absc][position+3*epaiss]   =0
                img_nombre[hauteur-coef_1+absc][position+1+3*epaiss] =0
                img_nombre[hauteur-coef_1+absc][position+2+3*epaiss] =0

    elif str_n == "5" :
        for ordonne in range (36*coef_img) :
            for epaiss in range(2*coef_img):
                img_nombre[hauteur-coef_1+epaiss][position+ordonne]    =0
                img_nombre[hauteur+epaiss][position+ordonne] =0
                img_nombre[hauteur+coef_1+epaiss][position+ordonne] =0
        for absc in range(21*coef_img):
            for epaiss in range(2*coef_img):
                img_nombre[hauteur-coef_1+absc][position+3*epaiss]   =0
                img_nombre[hauteur-coef_1+absc][position+1+3*epaiss] =0
                img_nombre[hauteur-coef_1+absc][position+2+3*epaiss] =0
                img_nombre[hauteur+absc+coef_img][position+coef_2+3*epaiss] =0
                img_nombre[hauteur+absc+coef_img][position+coef_2+1+3*epaiss] =0
                img_nombre[hauteur+absc+coef_img][position+coef_2+2+3*epaiss] =0

    elif str_n == "6" :
        for ordonne in range (36*coef_img) :
            for epaiss in range(2*coef_img):
                img_nombre[hauteur-coef_1+epaiss][position+ordonne]    =0
                img_nombre[hauteur+epaiss][position+ordonne] =0
                img_nombre[hauteur+coef_1+epaiss][position+ordonne] =0
        for absc in range(21*coef_img):
            for epaiss in range(2*coef_img):
                img_nombre[hauteur-coef_1+absc][position+3*epaiss]   =0
                img_nombre[hauteur-coef_1+absc][position+1+3*epaiss] =0
                img_nombre[hauteur-coef_1+absc][position+2+3*epaiss] =0
                img_nombre[hauteur+absc+coef_img][position+3*epaiss]   =0
                img_nombre[hauteur+absc+coef_img][position+1+3*epaiss] =0
                img_nombre[hauteur+absc+coef_img][position+2+3*epaiss] =0
                img_nombre[hauteur+absc+coef_img][position+coef_2+3*epaiss] =0
                img_nombre[hauteur+absc+coef_img][position+coef_2+1+3*epaiss]=0
                img_nombre[hauteur+absc+coef_img][position+coef_2+2+3*epaiss]=0

    elif str_n == "7" :
        for ordonne in range (36*coef_img) :
            for epaiss in range(2*coef_img):
                img_nombre[hauteur+epaiss-coef_1][position+ordonne]    =0
        for absc in range(coef_3+epais_taille):
            for epaiss in range(2*coef_img):
                img_nombre[hauteur+absc-coef_1][position+coef_2+3*epaiss] =0
                img_nombre[hauteur+absc-coef_1][position+coef_2+1+3*epaiss]=0
                img_nombre[hauteur+absc-coef_1][position+coef_2+2+3*epaiss]=0

    elif str_n == "8" :
        for ordonne in range (36*coef_img) :
            for epaiss in range(2*coef_img):
                img_nombre[hauteur-coef_1+epaiss][position+ordonne]    =0
                img_nombre[hauteur+epaiss][position+ordonne] =0
                img_nombre[hauteur+coef_1+epaiss][position+ordonne] =0
        for absc in range(coef_3+epais_taille):
            for epaiss in range(2*coef_img):
                img_nombre[hauteur-coef_1+absc][position+3*epaiss]   =0
                img_nombre[hauteur-coef_1+absc][position+1+3*epaiss] =0
                img_nombre[hauteur-coef_1+absc][position+2+3*epaiss] =0
                img_nombre[hauteur-coef_1+absc][position+coef_2+3*epaiss] =0
                img_nombre[hauteur-coef_1+absc][position+coef_2+1+3*epaiss]=0
                img_nombre[hauteur-coef_1+absc][position+coef_2+2+3*epaiss]=0

    elif str_n == "9" :
        for ordonne in range (36*coef_img) :
            for epaiss in range(2*coef_img):
                img_nombre[hauteur-coef_1+epaiss][position+ordonne]    =0
                img_nombre[hauteur+epaiss][position+ordonne] =0
                img_nombre[hauteur+coef_1+epaiss][position+ordonne] =0
        for absc in range(21*coef_img):
            for epaiss in range(2*coef_img):
                img_nombre[hauteur-coef_1+absc][position+3*epaiss]   =0
                img_nombre[hauteur-coef_1+absc][position+1+3*epaiss] =0
                img_nombre[hauteur-coef_1+absc][position+2+3*epaiss] =0
                img_nombre[hauteur-coef_1+absc][position+coef_2+3*epaiss] =0
                img_nombre[hauteur-coef_1+absc][position+coef_2+1+3*epaiss]=0
                img_nombre[hauteur-coef_1+absc][position+coef_2+2+3*epaiss]=0
                img_nombre[hauteur+absc+coef_img][position+coef_2+3*epaiss]=0
                img_nombre[hauteur+absc+coef_img][position+coef_2+1+3*epaiss]=0
                img_nombre[hauteur+absc+coef_img][position+coef_2+2+3*epaiss]=0


def _affichage_nombres_(nb_pixl,nb_dec,arr_unite_pi,arr_dec_pi,i):
    img_nombre=ones((nb_pixl,3*nb_pixl), dtype=int)
#Ceci nous permet de définir la taille et le centrage de l'image
    larg=3*nb_pixl
    coef_img=int((nb_pixl+350)/400)
    taille_image =30*coef_img*((nb_dec+1)*(1.38))
    position =int(3*(larg-taille_image-4*coef_img+6)/2//3)+1
    while position + 1.05*taille_image > 3*nb_pixl and coef_img>0:
        coef_img-=1
        taille_image =30*coef_img*((nb_dec+1)*(1.38))
        position =int(3*(larg-taille_image-4*coef_img+6)/2//3)+1
    hauteur=int(nb_pixl/2)
#Place à l'écriture de M
#on écrit d'abord l'unité de pi
    if coef_img>0 :
        _ecriture_(img_nombre,str(arr_unite_pi),hauteur, position,coef_img)
        position+=11*coef_img

#on dessine le point
        for epaisseur in range(2*coef_img):
            for ordonne in range (6*coef_img) :
                img_nombre[hauteur+20*coef_img+epaisseur][position+ordonne+28*coef_img] = 0
        position-= -coef_img

#on écrit maintenant les décimales
        for k in range (nb_dec):
            position+=42*coef_img
            if k<len(str(arr_dec_pi)):
                str__nb=str(arr_dec_pi)[k]
                _ecriture_(img_nombre,str__nb,hauteur, position,coef_img)
            else:
                _ecriture_(img_nombre,"0",hauteur, position,coef_img)

#exception si le nombre ne rentre pas dans  l'image
    elif i==0 :
        print("\n\nL'image est trop petite : impossible", end="")
        print(" d'afficher la valeur approché de pi au centre de l'image")
        print("\n\nVeuillez réésayer avec une taille d'image plus", end="")
        print(" grande ou un nombre de décimales plus petit\n\n")

    return img_nombre



def generate_ppm_file(l_nb_pts,nb_pixl,nb_dec,tab_ppm,comptage_pts,i):
    for _ in range (l_nb_pts[i], l_nb_pts[i+1]):
        sim_pt = simulator._points_(nb_pixl)
        tab_ppm[sim_pt[1][0]][3*sim_pt[1][1]]=(2-sim_pt[1][2])*100
        tab_ppm[sim_pt[1][0]][3*sim_pt[1][1]+1]=(sim_pt[1][2]-1)*250
        comptage_pts+=sim_pt[0]
    arr_unite_pi = int(4*comptage_pts/l_nb_pts[i+1])
    arr_dec_pi = int((4*comptage_pts/l_nb_pts[i+1]-arr_unite_pi) * 10**(nb_dec))

    img_nombre=_affichage_nombres_(nb_pixl,nb_dec,arr_unite_pi,arr_dec_pi,i)
    tab_final =reshape(tab_ppm*img_nombre, (product(tab_ppm.shape),))

    fichier_name=f'/out/img{i}_{arr_unite_pi}-{arr_dec_pi}.ppm'
    out = open(abspath(".") + fichier_name, 'wb')
    out.write(("P6 "+str(nb_pixl)+ " " + str(nb_pixl)+ " 255 ").encode() + bytes(list(tab_final)))
    out.close()
    return [fichier_name, comptage_pts]







bool_1=len(argv)!=4 or not str.isdigit(argv[1]+argv[2]+argv[3])
if  bool_1 or int(argv[1])*int(argv[2])==0:
    print("\n\n     ERREUR")
    print(" \nVeuillez entrer une ligne de commande de la forme :")
    print("\n     python3 (facultatif) " + argv[0]+ " nb_pixels nb_pts nb_dec_de_pi")
    print("\navec nb_pixels, nb_pts, nb_dec_de_pi, des entiers, ", end="")
    print("strictement positifs pour les deux premiers, et positif pour le second\n\n")
else :
    nb_pix = int(argv[1])
    nb_pt = int(argv[2])
    nb_decim = int(argv[3])
    gif_pi=[]
    list_nb_pt=linspace(0,nb_pt,11, dtype=int)
    tableau_ppm=255*ones((nb_pix,3*nb_pix), dtype=int)
    COMPT_PTS=0
    for m in range (10):
        [nom_fichier,COMPT_PTS]=generate_ppm_file(list_nb_pt,nb_pix,nb_decim,tableau_ppm,COMPT_PTS,m)
        gif_pi.append("." +nom_fichier)
    cmd=['convert','-delay','100','-loop','0' ] + gif_pi + ['Monte_Carlo.GIF']
    GIF=subprocess.call(cmd)
