#coding:utf-8
from math import *
import random
from threading import Thread
import time

#************************* Class Producer ********************************


class Producer :
#-- Fonction qui génére un nombre aléatoire en 10 et 99 ------------------
    def randomNumber(self) :
        return random.randint(10,99)
#-- Fonction qui consiste à mettre le thread en pause --------------------
    def wait(self) :
        time.sleep(3)