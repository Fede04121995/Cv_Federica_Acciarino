import ClasseLibro
class Libreria:
    
    
    def __init__(self, catalogo):
        self.catalogo = []

    def aggiungi_libro(self, l):
        self.catalogo.append(l)
        print(f"il libro {l.titolo} è stato aggiunto")
        
    def rimuovi_libro(self, l):
        self.catalogo.remove(l) 
        
    def cerca_per_titolo(self):
        
        
        pass  
    
    def mostra_catalogo():
        pass