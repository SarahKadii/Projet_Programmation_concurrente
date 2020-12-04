#coding:utf-8
from math import *
import random
from threading import Thread
import time

#************************* Class Consumer *****************************

class Consumer:
    def __init__(self, rnumber):
        self.number = rnumber
#-- Fonction qui affiche un nombre pris en paramètres -----------------
    def displayNumber(self):
        return self.number
#-- Fonction qui consiste à mettre le thread en pause -----------------
    def wait(self) :
        time.sleep(1)