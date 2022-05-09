
import random
from turtle import position

import pygame
from pygame.math import Vector2
from creep import Creep

import core


class Ennemi:
    def __init__(self):
        self.position = Vector2(random.randint(0,1295),random.randint(0,995))
        self.rayon = 50
        self.nourriture = 1
        self.couleur = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        self.masse = 100
        self.vitesse = Vector2(0, 0)
        self.acceleration = Vector2(0, 0)
        self.maxacc = 100
        self.l0 = 10
        self.k = 0.001
        self.vitessmin = 1
        self.vitessmax = 4
        self.taillemax = 300
        core.memory("c",Creep())
        self.vision = 100

    def afficher(self):
        core.Draw.circle(self.couleur, self.position, self.rayon)


 # creation du deplacement de l'ennemi
 #    def deplacement(self):



'''
    #creation du manger des ennemi sur creep
    for p in creep: 
        if p.position.distance_to(self.position) < self.vision
            creepdansvision.append(p)
            if p.position.distance_to(self.position) < distancecreep :
                cible = p
                distancecreep  = p.position.distance_to(self.position)
'''

