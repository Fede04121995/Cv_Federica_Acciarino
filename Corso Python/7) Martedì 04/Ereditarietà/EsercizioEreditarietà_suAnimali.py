class Animale2:

    def __init__(self, nome, età):
        self.nome = nome
        self.età = età
        
    def fai_suono(self):
        print(f"{self.nome} fa suono generico")
        
        
        
class Leone(Animale2):

    def __init__(self, nome, età, criniera):
        super().__init__(nome, età)  # Richiama il costruttore della classe madre
        self.criniera = criniera  # Attributo specifico


    def fai_suono(self):
        print(f"{self.nome} ruggisce fortemente!")  # Metodo specifico

    def caccia(self):
        print(f"{self.nome} sta cacciando nella savana.")  # Metodo specifico
    
  


class Giraffa(Animale2):
    
    def __init__(self, nome, età, collo):
        super().__init__(nome, età)  
        self.collo = collo  

    def fai_suono(self):
        print(f"{self.nome} giraffa fortemente!")  

    def mangia(self):
        print(f"{self.nome} sta mangiando.")  
    


class Pinguino(Animale2):
    
    def __init__(self, nome, età, ali):
        super().__init__(nome, età)  
        self.ali = ali 

    def fai_suono(self):
        print(f"{self.nome} pinguina fortemente!")  

    def nuota(self):
        print(f"{self.nome} sta nuotando.")  

leone = Leone("Simba", 5, "folta")
giraffa = Giraffa("Raffa", 7, "lungo")
pinguino = Pinguino("Nino", 3, "piccole")

leone.fai_suono()
leone.caccia()

giraffa.fai_suono()
giraffa.mangia()

pinguino.fai_suono()
pinguino.nuota()