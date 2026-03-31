
from Models import ModuloBase as mb


class ModuloAvanzato(mb):
    def salva_excel(self):
        print("Salvataggio personalizzato")
        super().salva_excel()