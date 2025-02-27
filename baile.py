def mover_cadera(lado, repetición):
    for i in range(repetición):
        for j in range(lado):
            print("muevo cadera hacia la derecha")
        for z in range(lado):
            print("muevo cadera hacia la izquierda")

def salto (lado, repetición):
    for i in range(repetición):
        for j in range(lado):
            print("salto adelante")
        for z in range(lado):
            print("salto atrás")

def salto2 (lado, repetición):
        for i in range(repetición):
            for j in range(lado):
                print("salto adelante derecha")
            for z in range(lado):
                print("salto adelante izquierda")

def agacharse (lado, repetición):
        for i in range(repetición):
            for j in range(lado):
                print("me agacho")

def subo (lado, repetición):
        for i in range(repetición):
            for j in range(lado):
                print("me paro")
                
def vuelta (lado, repetición):
        for i in range(repetición):
            for j in range(lado):
                print("doy una vuelta")         
                     
def brazo (lado, repetición):
        for i in range(repetición):
            for j in range(lado):
                print("alzo un brazo")      

agacharse(1,1)
subo(1,1)
vuelta(1,1)
mover_cadera(1,4)
salto(2,1)
brazo(1,1)
mover_cadera(1,4)
salto2(2,1)