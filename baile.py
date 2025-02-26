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

mover_cadera(1,4)
salto(2,1)
mover_cadera(1,4)
salto2(2,1)