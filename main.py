#coding:utf-8
from math import *
import random
import time
import threading 
from producer import *
from consumer import *

#************************** Fonction main *********************************************************

if __name__ == "__main__":
#-- Initialisation d'une liste vide qui représente la mémoire partagée ----------------------------
    listOfData = []

#** Class du thread qui instancie la class "Producer" *********************************************
    class TProducer(Thread):
        def __init__(self):
            Thread.__init__(self)
            self.lock = threading.Lock()
#------ Ajout du nombre généré dans la mémoire partagée -------------------------------------------
        def run(self):
            self.lock.acquire()
            prd = Producer()
            listOfData.append(prd.randomNumber())
            print("Voici la liste après la production de valeurs : {} \n ".format(listOfData))
            self.lock.release()
            prd.wait()

#** Class du thread qui instancie la class Consumer ***********************************************
    class TConsumer(Thread):
        def __init__(self):
            Thread.__init__(self)
            self.lock = threading.Lock()
#------ Consommateur qui récupère une ou plusieurs valeur de la mémoire partagée puis supprime cette
#       valeur de la liste (mémoire partagée) ------------------------------------------------------
        def run(self):
            if (len(listOfData) == 0):
                print("La liste est vide \n")
            else : 
                self.lock.acquire()
                cns = Consumer(listOfData[0])
                listOfData.pop(0)
                print("Voici la liste après la consommation de données : {} \n".format(listOfData))
                self.lock.release()
                cns.wait()
                
#** Création et lancement des Threads **************************************************************
    for i in range (0 ,50):
        rnd = random.randint(1,2)
        if (rnd == 1):
            thP = TProducer()
            thP.start()
        else :
            thC = TConsumer()
            thC.start() 

#-- Attente de la fin des Threads ------------------------------------------------------------------
    thP.join()
    thC.join()    
    
    
        
        
