import time

def simular_reloj_comprension(segundos):
    horas = 0
    minutos = 0
    segundos_restantes = 0
    
    for _ in range(segundos):
       
        print(f"{horas:02d}:{minutos:02d}:{segundos_restantes:02d}", end="\r")
        
      
        time.sleep(1)
        segundos_restantes += 1
        
        
        if segundos_restantes == 60:
            segundos_restantes = 0
            minutos += 1
        
        
        if minutos == 60:
            minutos = 0
            horas += 1

def mostrar_reloj_comprension():
    while True:
        
        segundos = int(input("Ingrese la cantidad de segundos para simular el reloj: "))
        
       
        simular_reloj_comprension(segundos)
        
        
        continuar = input("¿Desea simular otro reloj? (s/n): ").lower()
        if continuar != 's':
            break


mostrar_reloj_comprension()








import time

def simular_reloj_lambda(segundos):
    horas = 0
    minutos = 0
    segundos_restantes = 0
    
    
    mostrar_tiempo = lambda horas, minutos, segundos: print(f"{horas:02d}:{minutos:02d}:{segundos:02d}", end="\r")
    
    for _ in range(segundos):
     
        mostrar_tiempo(horas, minutos, segundos_restantes)
        
        
        time.sleep(1)
        segundos_restantes += 1
        
       
        if segundos_restantes == 60:
            segundos_restantes = 0
            minutos += 1
        
       
        if minutos == 60:
            minutos = 0
            horas += 1

def mostrar_reloj_lambda():
    while True:

        segundos = int(input("Ingrese la cantidad de segundos para simular el reloj: "))
        
      
        simular_reloj_lambda(segundos)
        
        
        continuar = input("¿Desea simular otro reloj? (s/n): ").lower()
        if continuar != 's':
            break


mostrar_reloj_lambda()

