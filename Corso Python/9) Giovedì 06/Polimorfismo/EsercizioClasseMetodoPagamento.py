class MetodoPagamento:
    def effettua_pagamento(self,importo):
        return f"Pagamento effettuato di {importo}€ con metodo generico."



class CartaDiCredito(MetodoPagamento):
    def __init__(self, numero_carta, titolare):
        self.numero_carta = numero_carta
        self.titolare = titolare
    
    def effettua_pagamento(self,importo):
        return f"Pagamento di {importo} effettuato con carta di credito ({self.numero_carta}) titolare {self.titolare}."




class PayPal(MetodoPagamento):
    def __init__(self, email):
        self.email = email
        
    def effettua_pagamento(self,importo):
        return f"Pagamento di {importo} effettuato tramite PayPal dall'account {self.email}."


    
    
class BonificoBancario(MetodoPagamento):
    def __init__(self, iban, intestatario):
        self.iban = iban
        self.intestatario = intestatario
    
    def effettua_pagamento(self,importo):
        return f"Pagamento di {importo} effettuato con bonifico all'IBAN {self.iban} intestato a {self.intestatario}."

carta = CartaDiCredito("12334444555", "Federica Acciarino")
paypal = PayPal("federica@gmail.com")
bonifico = BonificoBancario("IT 98239174834823978","Federica Acciarino")

#print(carta.effettua_pagamento(30))
#print(paypal.effettua_pagamento(40))
#print(bonifico.effettua_pagamento(50))

class GestorePagamenti:
    def __init__(self, metodo_pagamento):
        self.metodo_pagamento = metodo_pagamento
    
    def esegui_pagamento(self, importo):
        self.importo = importo
        return self.metodo_pagamento.effettua_pagamento(importo)
        
gestore_carta = GestorePagamenti(carta)
gestore_paypal = GestorePagamenti(paypal)
gestore_bonifico = GestorePagamenti(bonifico)

print(gestore_carta.esegui_pagamento(30))  
print(gestore_paypal.esegui_pagamento(40))  
print(gestore_bonifico.esegui_pagamento(50)) 
