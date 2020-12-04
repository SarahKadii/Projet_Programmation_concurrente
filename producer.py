#coding:utf-8
from math import *
import random

class Producer :
    def __init__(self):
        print("Création d'un producteur \n")

    def randomNumber(self) :
        return random.randint(1,100)

p1 = Producer()
print("Le nb random afficher par le producer 1 est : {}".format(p1.randomNumber()))