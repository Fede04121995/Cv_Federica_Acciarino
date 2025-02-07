from abc import ABC, abstractmethod

class Impiegato(ABC):
    @abstractmethod
    def __init__(self,nome, cognome, stipendio_base):
        self.nome = nome
        self.cognome = cognome
        self.stipendio_base = stipendio_base
        
    def calcola_stipendio(self):
        pass
        
        
class ImpiegatoFisso(Impiegato):
    def __init__(self, nome, cognome, stipendio_base):
        super().__init__(nome, cognome, stipendio_base)
    
    def calcola_stipendio(self):
        return self.stipendio_base


class ImpiegatoAProvvigione(Impiegato):
    def __init__(self, nome, cognome, stipendio_base, vendite, percentuale_bonus):
        super().__init__(nome, cognome, stipendio_base)
        self.vendite = vendite
        self.percentuale_bonus = percentuale_bonus
    
    def calcola_stipendio(self):
        bonus = self.vendite * (self.percentuale_bonus / 100)
        return self.stipendio_base + bonus
    
    
def stampa_info_impiegato(impiegato):
    stipendio = impiegato.calcola_stipendio()
    print(f"Nome: {impiegato.nome} {impiegato.cognome}")
    print(f"Stipendio: {stipendio}€")
    print("-" * 30)
   
    
impiegato_fisso = ImpiegatoFisso("Federica", "Acciarino", 2000)
impiegato_provvigione = ImpiegatoAProvvigione("Federica", "Rossi", 2000, vendite=10, percentuale_bonus=20)

print(f"Stipendio di {impiegato_fisso.nome} {impiegato_fisso.cognome}: {impiegato_fisso.calcola_stipendio()}")
print(f"Stipendio di {impiegato_provvigione.nome} {impiegato_provvigione.cognome}: {impiegato_provvigione.calcola_stipendio()}€")