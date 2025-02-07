class Libro:
    def __init__(self, titolo, autore, pagine, isbn):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine
        self.isbn = isbn
       
    def descrizione(self):
        print(f"il libro {self.titolo} è stato scritto da {self.autore} ed ha {self.pagine} pagine e il suo isbn è: {self.isbn}")
        
l = Libro("La mia vita", "Federica", "300", "1")
l.descrizione()
