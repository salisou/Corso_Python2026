#class Persone:
#   def staluta(self): 
#        print("Ciao sono una Moussa")

# self => rapresenta l'oggetto stesso
# serve per accedere ai dati dell'oggetto

class Persona:
    # Construttore della classe con parametri
    def __init__(self, nome, eta): 
        self.nome = nome 
        self.eta = eta   
    
    # Funzione o Metodo
    def saluta(self):    
        print(f"Ciao, mi chiamo {self.nome}, ho {self.eta} anni")



# stampa il contenuto della classe persona

p1 = Persona("Carlo", 35)
p1.saluta()