class Ram:
    def __init__ (self, velox):
        self.velox = velox
        
    def veloce(self):
        print(f"Questa Ram è pari a {self.velox}") 
        
class Cpu:
    def __init__ (self, intel) :
        self.intel = intel  
        
    def processore(self):
        print(f"Il processore è pari ad un intel {self.intel}")
        
        
class Computer(Ram, Cpu):
    def __init__(self, velox, intel, peso):
        Ram.__init__(self, velox)  
        Cpu.__init__(self, intel) 
        self.peso = peso
        
    def pesante(self):
        print(f"Il peso di questo computer è di {self.peso} kg")
        
        
ram = Ram("32GB")
cpu = Cpu("i7")
pc = Computer("32GB", "i7", "1,5")

ram.veloce()
cpu.processore()
pc.pesante()