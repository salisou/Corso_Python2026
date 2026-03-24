"""
Struttura del corso
    1 Cos’è la programmazione OOP
    2 Classi e oggetti
    3 Attributi e metodi
    4 Il costruttore (__init__)
    5 Incapsulamento
    6 Ereditarietà
    7 Polimorfismo
    8 Metodi speciali (dunder methods)
    9 Progetto finale guidato
"""

# self => rapresenta l'oggetto stesso
# serve per accedere ai dati dell'oggetto
class Animale:
    def verso(self):
        print("Miao")

class Cane:
    def abbaia(self):
        print("bauu!")
        
        
a1 = Animale()
b1 = Cane()


# b1.abbaia() 
# a1.verso()


# Incapsulamento
# public  self.name
# private self._noe

# ==, +=, -= ...
# Creare una classe Conto bancario
class ContoBancario:
    def __init__(self, saldo):
        self._saldo = saldo
    
    def deposito(self, importo):
        self._saldo += importo

    def mostra_saldo(self):
        print(f"Saldo attuale: {self._saldo}€")
    
# Stampare il conto corrente
euro=(1000)

conto=ContoBancario(euro)
conto.mostra_saldo()

conto.deposito(10000)
conto.mostra_saldo()
print("\n")

# Nome cognome, Email, DataNascita, CodiceFiscale
class Studente:
    def __init__(self, nome, cognome, email, data_nascita, codice_fiscale): 
        self._nome = nome 
        self._cognome = cognome
        self._email = email
        self._data_nascita = data_nascita
        self._codice_fiscale = codice_fiscale
        
    def __str__(self):
        return f"{self._nome}, {self._cognome}, {self._email}, {self._data_nascita}, {self._codice_fiscale}"
    
    def mostra_dati(self):
        print(f"{self._nome}, {self._cognome}, {self._email}")
       
        """
    def mostra_dati(self):
        print(f"{self._nome},{self._cognome},{self._email}")
        print("Nome: ", self._nome)
        print("Cognome: ", self._cognome)
        print("Email: ", self._email)
        print("Codice Fiscale: ", self._codice_fiscale)
        print("Data Nascita: ", self._data_nascita)
        """
        

stu1 = Studente("Cosimo", "Pastore", "cos.past@gmail.com", "07-03-1987", "CSMHJKERW45687F4\n")
stu1.mostra_dati()

# stampa lo studente
#print(stu1)

# Questa vlasse gestisce più studenti
class RegistroStudenti:
    def __init__(self):
        self._ListaStudenti = []
    
    def aggiungi_studente(self, studente):
        self._ListaStudenti.append(studente)
        
    def mostra_studenti(self):
        for s in self._ListaStudenti:
            print(s)
    
    def cerca_per_email(self, email):
        for st in self._ListaStudenti:
            if st._email == email:
                return st
        return None

    def modifica_email(self, vecchio_email, nuovo_email):
        stud = self.cerca_per_email(vecchio_email)
        if stud:
            stud._email = nuovo_email
            return True
        return False

    def elimina_studente(self, email):
        for stu in self._ListaStudenti:
            if stu._email == email:
                self._ListaStudenti.remove(stu)
                return True
            return False
    
    


# Creare un registro
registro = RegistroStudenti()

# Creare Studenti
studente1 = Studente("Federica", "De Angelis", "federica@mail.com", "30/04/1979", "DNGFRC79D70H501H")
studente2 = Studente("Carlo", "caputo", "carlo@caputo", "13/05/1988", "cptcrl88e13f104j")
studente3 = Studente("Pietro", "Cammise", "pietro@gmail.com", "1970-01-01", "BIPPPP80A01A123A")
studente4 = Studente("Walid", "boussad", "walid@gmail.com","01/11/2000", "BSSWLD00M12H501X")
studente5 = Studente("Pierfrancesco","melle","pier26@gmail.com","26/07/2000","mllpfr993467126g")
studente6 = Studente("Cosimo", "Pastore", "cos.past@gmail.com", "07-03-1987", "CSMHJKERW45687F4")

# Aggiungere nel registro
registro.aggiungi_studente(studente1)
registro.aggiungi_studente(studente2)
registro.aggiungi_studente(studente3)
registro.aggiungi_studente(studente4)
registro.aggiungi_studente(studente5)
registro.aggiungi_studente(studente6)

# Mostrare tutti i deti degli studenti 
registro.mostra_studenti()

# Cercare lo studente per email

studente = registro.cerca_per_email("federica@mail.com")

if studente:
    print(f"\nTrovato: {studente}")
else:
    print("Non trovato")

# modificare l'email

# eliminare lo studente per mail 
