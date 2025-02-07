class Ristorante:
    def __init__(self, nome, tipo_cucina):
        self.nome = nome 
        self.tipo_cucina = tipo_cucina
        self.aperto = False
        self.lista_piatti = []
        self.lista_prezzi = []
        
        
    def descrivi_ristorante(self):
        print(f"Il ristorante {self.nome} è una {self.tipo_cucina}")
        
       
    def stato_apertura(self):
        if self.aperto :
            print(f"{self.nome} è aperto")
        else:
            print(f"{self.nome} è chiusa")
            
    def apri_ristorante(self):
        self.aperto = True
        print("Il ristorante è ora aperto")
        
    def chiudi_ristorante(self):
        self.aperto = True
        print("Il ristorante è ora chiuso")                    
        
    def aggiungi_piatto(self):
        scelta_piatto = input("Aggiungi piatto:")
        scelta_prezzo = input("Aggiungi prezzo")
        
        self.lista_piatti.append(scelta_piatto)
        self.lista_prezzi.append(scelta_prezzo)
        print(f"Il Piatto {scelta_piatto} è stato aggiunto con prezzo {scelta_prezzo}€")
        
    def rimuovi_dal_menu(self, piatto):
        if piatto in self.menu_piatti:
            indice = self.menu_piatti.index(piatto)
            self.menu_piatti.pop(indice)
            self.menu_prezzi.pop(indice)
            print(f"Rimosso {piatto} dal menu.")
        else:
            print(f"{piatto} non è presente nel menu.")  
        
    def crea_menu(self):
        menu = list(zip(self.lista_piatti, self.lista_prezzi))
        print(menu)      
    
            
    
        
        
r = Ristorante("La Pizzeria", "pizzeria")          
r.descrivi_ristorante()
r.stato_apertura()
r.apri_ristorante()
r.chiudi_ristorante()
r.aggiungi_piatto()
r.crea_menu()
r.rimuovi_dal_menu()
