class Prodotto:
    def __init__(self, nome, costo_produzione, prezzo_vendita):
        # Inizializza gli attributi comuni a tutti i prodotti
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita
        
    def calcola_profitto(self):
        # Ritorna la differenza tra il prezzo di vendita e il costo di produzione
        return self.prezzo_vendita - self.costo_produzione    