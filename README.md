# Monte Carlo

Premier projet d'informatique, une simulation de Monte Carlo pour approcher pi avec un certain nombre de décimales + un joli GIF pour visualiser tout ça.

Lancer `python simulator.py` avec les arguments qu'il faut :
  * nb_pixel : largeur de l'image du GIF
  * nb_pts : nombre de points pour la simulation
  * nb_dec_de_pi : le nombre de décimales de pi souhaité

Il y a un semblant d'optimisation mais cela reste très modeste, donc commencez avec de petits nombres ^^

  
  \  
  \  
  \  
  \  


**Voici le compte rendu de l'époque (c'est un peu barbant et peu utile) :** 

Le rendu comporte 2 fichiers, simulator.py et approximate_pi.py, comme demandé par le sujet.
Ce qui en suit, présentera le contenu, la performance et les difficultés rencontrées lors de la création de ces deux fichiers.  

simulator.py possède une fonction _point_ qui prend en argument le nombre de pixels souhaités pour le rendu final. Cet argument n'est là que pour alléger le fichier approximate_pi en retournant à chaque fois une liste [compt,[x,y,z]], avec:
	* x, y les coordonnées du point dans le carré de taille "nombre de pixels"
	* z = 1 si le point est dans le cercle, 2 sinon (z va nous permettre de donner une couleur en particulier pour les points dans et hors du cercle)
	* compt = 1 si le point est dans le cercle, 0 sinon. Cela va nous permettre de compter le nombre de point dans le cercle.
Cel est possible grâce à la fonction uniform du module random qui nous donne deux points dans [-1,1] x' et y'. Le calcul de la distance du point (x',y') par rapport à l'origine nous permettra de savoir si le point est effectivement dans le cercle ou non).
simulator.py contient aussi une exeption dans le cas où il serait lancé en ligne de commande. En cas d'erreur, s'affichera ce qu'il faudra rentrer pour le bon fonctionnement du code. Dans le cas où la syntaxe serait respecté, le programme appellera _points_ n fois pour compter le nombre de points dans le cercle et afficher un résultat.  

\  
Passons maintenant au fichier simulator_pi.py. Il contient trois fonctions :  
	* _ecriture_ qui permet d'écrire les chiffres de 0 à 1  
	* _affichage_nombres_ qui permet de générer l'image centrale avec la valeur de pi demandé  
	* generate_ppm_file qui permet de créer une image .PPM comme précisé.  
\  
Nous allons les détailler de bas en haut, pour rester cohérent en terme de chronologie. Commençons par la fonction generate_ppm_file.
Pour cette fonction, beaucoup d'arguments sont demandés :   
	* l_nb_pts : la liste du nombre de points qu'on souhaite tracer  
	* nb_pixl : la taille de l'image souhaitée  
	* nb_dec : le nombre de décimales pour la valeur de pi demandée   
	* tab_ppm : un tableau de (nb_pixl x 3nb_pixl) qu'on détaillera un peu plus tard  
	* comptage_pts : qui est le compteur de points dans le cercle  
	* i représente le numéro de l'image (de 0 à 9 inclus)    
Pour cette fonction qui a pour fonction première de créer une image .PPM, nous avons opté pour l'utilisation d'un tableau de type array (le fameux tab_ppm) pour limiter la mémoire et diminuer la complexité. En effet, tout était parti pour une longue liste des points à dessiner (de longueur n), et de les écrire sur le fichier .PPM, en allant chercher les points un par un dans la liste préalablement triée. C'était possible, mais le temps de calcul était à désirer (40s pour 1M de point sur une image de 800px*800px), et la complexité était à revoir notamment à cause des deux tris fusion (en nlog(n)) et de la recherche, certes dichotomique mais très longue de chaque point de l'image (en l'occurrence 800*800=160000 points).
Ainsi, un grand tableau tab_ppm comprenant chaque valeur à écrire dans le fichier .PPM était une bien meilleure solution. Cela nous permet d'accéder à chaque valeur et de la modifier à notre guise, avec moins de temps et moins d'espace car connaissant déjà la dimension de l'image, un tableau étant préférable à une liste sur Python.   
Ce tableau sera conservé tout le long de la création des 10 images et ne comportera que les points à tracer (mais pas l'image centrale).  

Avant d'utiliser la fonction generate_ppm_file, nos aurions préalablement créé un tableau de 11 points list_nb_pt, contenant les intervalles de points nécessaires pour chaque image. Ainsi, nous savons combien de fois faut-il appeler la fonction _point_ de simulator.py pour l'inscrire dans le tableau tab_ppm. Nous n'oublions pas de compter le nombre de points dans le cercle durant l'utilisation de _point_, et à l'aide de list_nb_pt, nous savions exactement combien de points ont été mis dans list_ppm jusque là : nous pouvions calculer la valeur approchée de pi.   
/  
C'est là qu'intervient la fonction affichage nombre qui permettra à l'aide de la valeur de pi, d'écrire la valeur au centre de l'image. Il est fait en sorte que la taille et l'épaisseur de l'affichage dépendent de la taille de l'image mais aussi du nombre de décimale de pi que l'on veut afficher : dans le cas où l'affichage n'est pas possible : soit la taille diminue, soit un message d'erreur est affiché. La fonction créer un tableau de la même taille que tab_ppm qui comportera des 1 partout, sauf aux endroits où l'on veut qu'il y ait des pixels noirs. Grâce à la fonction _ecriture_, nous placions les bons chiffres au bon endroit. Ce tableau img_nombre sera retourné et multiplié par la fonction product avec le tableau tab_ppm. Les termes se multiplient entre eux, plaçant des 0 aux endroits où l'on veut du noir, et ne changeant pas les autres valeurs.   
/  
Pour la génération de l'image .PPM, nous avons opté pour le format P6 en bytes qui prend moins de place (le format P3 sur 255 prenait 9Mo pour chaque image, et le format P3 sur 1 prenait 3.7 Mo par image), donc après quelques recherches sur Internet, pas autant documenté sur le P6, nous avons pu convertir notre tableau en liste d'une dimension pour l'avoir ensuite en bytes.   
/  
Tous les noms des images seront placés dans une liste gif_pi, et la fonction subprocess.call permettra de transformer le tout en .gif.  
/  
La complexité est linéaire en fonction de la taille de l'image, et semble être meilleur que le linéaire en fonction du nombre de points souhaités. Il n'y a pas de variations significatives en fonction du nombre de décimales souhaitées.   
/  
Le programme pour une taille de 800x800px pour 1M de points avec 5 décimales prend 7s à tourner, créant des images à 1.8Mo sur un ordinateur sous Manjaro avec 16Go de RAM avoir mémoire SSD.  
