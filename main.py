#coding:utf-8
from math import *
import random
import time
import threading 
from producer import *
from consumer import *

#** Class du thread qui instancie la class "Producer" *************************************************************


class TProducer(Thread) :
    Producer().wait()
    cptP = 0
    def __init__(self) :
        Thread.__init__(self)
        self.lock = threading.Lock()
        TProducer.cptP += 1
        self.cptP = TProducer.cptP

#------ Ajout du nombre généré dans la mémoire partagée -----------------------------------------------------------
    def run(self) :
        self.lock.acquire()
        prd = Producer()
        listOfData.append(prd.randomNumber())
        print("*Production de la donnée   : {}  | Liste : {}\n".format(listOfData[len(listOfData) - 1],listOfData))
        prd.wait()
        self.lock.release()
        

#** Class du thread qui instancie la class Consumer ***************************************************************


class TConsumer(Thread) :
    cptC = 0
    nbThreadFinished = 0
    def __init__(self) :
        Thread.__init__(self)
        self.lock = threading.Lock()
        TConsumer.cptC += 1
        self.cptC = TConsumer.cptC
#------ Consommateur qui récupère une ou plusieurs valeur de la mémoire partagée puis supprime cette --------------
#       valeur de la liste (mémoire partagée) ---------------------------------------------------------------------
    def run(self) :
        while(True) :
#---------- Cas où la liste de données est vide -------------------------------------------------------------------
            if (len(listOfData) == 0) :
                if ((count_consumers - abs(count_consumers - count_producers) == TConsumer.nbThreadFinished) or 
                   ((count_consumers - 1) == TConsumer.nbThreadFinished)):
#------------------ Cas où le nombre de producteurs est inférieur ou égale au nombre de consommateurs -------------
                    if (count_producers <= count_consumers) :
                        if (count_producers == TProducer.cptP):
                            print("Toutes les données ont été consommées.\n")
                            quit()
#------------------ Cas où le nombre de producteurs est supérieur au nombre de consommateurs ----------------------
                    else:
#---------------------- Sous cas où le producteur courant est le dernier ------------------------------------------
                        if (count_producers == TProducer.cptP) :
                            print("Toutes les données restantes ont été consommées par le dernier consommateur.\n")
                            quit()
#---------- Cas où le consommateur consomme la donnée car la liste n'est pas vide ---------------------------------                             
            else:
                self.lock.acquire()
                cns = Consumer(listOfData[0])
                listOfData.pop(0)
                print("*Consommation de la donnée : {}  | Liste : {}\n".format(cns.displayNumber(), listOfData))
                if (self.cptC < count_consumers) :
                    TConsumer.nbThreadFinished += 1
                    break
                self.lock.release()

#************************** Fonction main *************************************************************************


if __name__ == "__main__" :
#-- Initialisation d'une liste vide qui représente la mémoire partagée --------------------------------------------
    listOfData = []
    count_producers = 6
    count_consumers = 6

#-- Création et lancement des Threads -----------------------------------------------------------------------------
    for i in range (0, count_consumers - 1) :
        thC = TConsumer()
        thC.start()
    for i in range (0, count_producers - 1) :
        thP = TProducer()
        thP.start()
    thC = TConsumer()
    thC.start()
    thP = TProducer()
    thP.start()
#-- Attente de la fin des Threads ---------------------------------------------------------------------------------
    thP.join()
    thC.join()
    print("Résultat du contenu de la liste après l'execution : {} \n".format(listOfData))