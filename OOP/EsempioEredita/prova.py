class Persona:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
    
    def __str__(self):
         return f"{self.nome} {self.cognome}"

    def Saluta(self):
        print(f"Ciao sono {self.nome}")
        

class Insegnante(Persona):
    def __init__(self, nome, cognome, materia):
        super().__init__(nome, cognome)
        self.materia = materia

    def __str__(self):
            return f"{self.nome} {self.cognome} {self.materia}"

persona = Persona("Walid", "Parentesi")
insegnante = Insegnante("Moussa", "Salisou", "Programmazione in python")
print(insegnante)

