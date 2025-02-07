import ClasseProdotto

class Abbigliamento:
    def __init__(self, nome, costo_produzione, prezzo_vendita, materiale):
        # Crea un'istanza di Prodotto per gestire gli attributi comuni
        self.prodotto = Prodotto(nome, costo_produzione, prezzo_vendita)
        self.materiale = materiale
