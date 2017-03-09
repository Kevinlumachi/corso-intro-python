from datetime import datetime

class Marca:

    def __init__(self, nome):
        self.nome = nome

    def __repr__(self):
        return "<Marca %s" % self.nome

class Automobile:
    
    def __init__(self, nome, anno, marca, consumo):
        anno = int(anno)        
        self.nome = nome
        self.anno = anno
        self.marca = Marca(marca)
        self.tempo = datetime.now().year - anno
        self.consumo = consumo 
        self.carburante = 30
    def __repr__(self):
        return "<Automobile %s>" % self.nome

    def rifornisci(self, litri):
        self.carburante += litri

    def consuma(self, litri):
        self.carburante -= litri


if __name__ == '__main__':
    import time  
    nome = raw_input('Nome della macchina: ')
    anno = raw_input('anno di fabbricazione (aaaa): ')
    while len(anno) !=4:
        print "Errore nel formato dell' anno!"
        anno = raw_input('anno di fabbricazione (aaaa): ')
    marca = raw_input("Nome della marca: ")
    consumo = raw_input("Quanto consuma al secondo: ")  
    mia_auto = Automobile(nome, anno, marca, consumo)
    print "Quindi possiedi una %s,%s" % (mia_auto.marca.nome, mia_auto.nome)
    
    
    print mia_auto
    print "Costruita nel %s" % mia_auto.anno
    
    print "E' stata costruita %s anni fa" % mia_auto.tempo
    print "Carburante: %s litri" % mia_auto.carburante

    mia_auto.rifornisci(30)
    print "Carburante: %s litri" % mia_auto.carburante

    secondi = 20
    while secondi > 0:
        mia_auto.consuma()
        if mia_auto.carburante <= 0:
            print "E' finita la benzina"
            break
        secondi -= 1
        time.sleep(1)
        print "Carburante: %s litri" % mia_auto.carburante
    
