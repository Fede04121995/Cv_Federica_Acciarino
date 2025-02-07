lista_valori = []
dizionario = {}

booleano = input("scegli se True o False")
numero = int(input("inserisci un numero intero"))
parola = str(input("inserisci il tuo nome"))

lista_valori.append(booleano)
lista_valori.append(numero)
lista_valori.append(parola)

dizionario["tipididato"] =  lista_valori

print(lista_valori)
print(dizionario)