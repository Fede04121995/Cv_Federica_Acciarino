class Posto:
    def __init__(self, numero, fila):
        self.__numero = numero
        self.__fila = fila
        self.__occupato = False
        
    def prenota(self):
        if(self.__occupato):
            print(f"Il posto {self.__fila}{self.__numero} è già occupato.")
        else:
            self.__occupato = True
            print(f"Posto {self.__fila}{self.__numero} ora prenotato.")
            
    def libera(self):
        if self.__occupato:
            self.__occupato = False
            print(f"Posto {self.__fila}{self.__numero} appena liberato.")
        else:
            print(f"Errore: Il posto {self.__fila}{self.__numero} non era prenotato.")
            
    def get_numero(self):
        return self.__numero

    def get_fila(self):
        return self.__fila

    def get_occupato(self):
        return self.__occupato
    
    
p1 = Posto(1, "A")
p1.prenota()
p1.libera()