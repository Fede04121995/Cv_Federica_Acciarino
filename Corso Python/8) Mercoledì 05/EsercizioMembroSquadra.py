class Squadra:
    def __init__(self, nome_squadra):
        self.nome_squadra = nome_squadra
        self.lista_giocatori = []
        self.lista_allenatori = []
        self.lista_assistenti = []
        
    def descrizione(self):
        print(f"La squadra {self.nome_squadra} è composta da:")
        print("\nGiocatori")
        for giocatore in self.lista_giocatori:
            print(giocatore)
            
        print("\nAllenatori:")
        for allenatore in self.lista_allenatori:
            print(allenatore)
        print("\nAssistenti")    
        for assistente in self.lista_assistenti:
            print(assistente)
    

class MembroSquadra:
    def __init__(self, nome, età,):
        self.nome = nome
        self.età = età
        
    def descrivi(self):
        return f"Il membro della squadra è {self.nome} ed ha {self.età} anni"
    

class Giocatore(MembroSquadra):
    def __init__(self, nome, età, ruolo, numero_maglia):
        super().__init__(nome, età)
        self.ruolo = ruolo
        self.numero_maglia = numero_maglia
        
    def gioca_partita(self):
        return f"Il giocatore {self.nome} con ruolo {self.ruolo} e numero alla maglia {self.numero_maglia} ha giocato la partita alle 12"
    
    def __str__(self):
        return f"{self.nome}, {self.età} anni, Ruolo: {self.ruolo}, Maglia: {self.numero_maglia}"
     

class Allenatore(MembroSquadra):
    def __init__(self, nome, età, anni_di_esperienza):
        super().__init__(nome, età)
        self.anni_di_esperienza = anni_di_esperienza
        
    def dirige_allenamento(self):
        return f"l'allenatore {self.nome} con {self.anni_di_esperienza} anni di esperienza, ha diretto molto bene"
    
    def __str__(self):
        return f"{self.nome}, {self.età} anni, Esperienza: {self.anni_di_esperienza} anni" 
     

class Assistente(MembroSquadra):
    def __init__(self, nome, età, specializzazione):
        super().__init__(nome,età)
        self.specializzazione = specializzazione
    
    def supporta_team(self):
        return f"L'assistente {self.nome} supporta la squadra come {self.specializzazione} "
    
    def __str__(self):
        return f"{self.nome}, {self.età} anni, Specializzazione: {self.specializzazione}"

     
squadra1 = Squadra("FederAccia")

scelta_giocatori = int(input("Quanti giocatori vuoi aggiungere?"))
for x in range(1, scelta_giocatori + 1): 
    nome_giocatore = input("Inserisci giocatore")
    età = int(input("Che età ha? :"))
    numero_maglia = int(input("con numero maglia ? :"))
    ruolo = input("Qual è il suo ruolo?")
    giocatore = Giocatore(nome_giocatore, età, ruolo, numero_maglia,)
    squadra1.lista_giocatori.append(giocatore) 
    

scelta_allenatori = int(input("Quanti allenatori ci sono?"))
for x in range(1, scelta_allenatori + 1): 
    nome_allenatore = input("Inserisci allenatore")
    età = int(input("Che età ha? :"))
    anni_di_esperienza = input("Quanti anni di esperienza ha")
    allenatore = Allenatore(nome_allenatore, età, anni_di_esperienza,)
    squadra1.lista_allenatori.append(allenatore) 
    


scelta_assistenti = int(input("Quanti assistenti ci sono?"))
for x in range(1, scelta_assistenti + 1): 
    nome_assistente = input("Inserisci assistente")
    età = int(input("Che età ha? :"))
    specializzazione = input("specializzazione?")
    assistente = Assistente(nome_assistente, età, specializzazione,)
    squadra1.lista_assistenti.append(assistente) 


squadra1.descrizione()
    
    