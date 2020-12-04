class Consumer:
    #Class consommateur 
    def __init__(self, rnumber):
        self.number = rnumber
        

    def displayNumber(self):
        return self.number

c1 = Consumer(3)
#J'affiche le nb qui a été entré dans le random
print("le nb rd est : {}".format(c1.displayNumber()))
