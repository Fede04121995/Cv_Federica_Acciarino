class Punto:
    x = 0
    y = 0


    def muovi(self, nuovo_x, nuovo_y):
        self.x = nuovo_x
        self.y = nuovo_y
        print("IL nuovo x è", nuovo_x)
        print("IL nuovo y è", nuovo_y)

    def distanza_org(self):
        if(self.x != 0 and self.y != 0):
            print("la distanza di x e y è", self.x, self.y)
        else:
            print("la distanza non esiste")

p = Punto()
p.muovi(5,6)
p.distanza_org()

distanza_punti = p.x - p.y
print(distanza_punti)


