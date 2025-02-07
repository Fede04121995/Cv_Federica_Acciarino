class Persona:
    __nome = "Mirko"
    _cognome = "Campari"
    
    
    def get_nome(self):
        return self.__nome
        
    def set_nome(self, n):
        self.__nome = n
        print(self.__nome)
    
    
mirko1 = Persona()
#print(mirko1.__nome)   # errore. non è accessibile. non è più visibile

print(mirko1.get_nome())
mirko1.set_nome("Paolo")
mirko1.get_nome()