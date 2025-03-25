def calcular_potencia_comprension(base, exponente):
  
    resultado = 1
    for _ in range(exponente):
        resultado *= base
    return resultado

def calcular_potencia_comprension_usuario():
    while True:
 
        base = float(input("Ingrese la base: "))
        exponente = int(input("Ingrese el exponente: "))
        
     
        resultado = calcular_potencia_comprension(base, exponente)
        print(f"{base} elevado a {exponente} es: {resultado}")
        

        continuar = input("¿Desea calcular otra potencia? (s/n): ").lower()
        if continuar != 's':
            break


calcular_potencia_comprension_usuario()













from functools import reduce

def calcular_potencia_lambda(base, exponente):
    
    return reduce(lambda x, _: x * base, range(exponente), 1)

def calcular_potencia_lambda_usuario():
    while True:
      
        base = float(input("Ingrese la base: "))
        exponente = int(input("Ingrese el exponente: "))
        
        
        resultado = calcular_potencia_lambda(base, exponente)
        print(f"{base} elevado a {exponente} es: {resultado}")
  
        continuar = input("¿Desea calcular otra potencia? (s/n): ").lower()
        if continuar != 's':
            break


calcular_potencia_lambda_usuario()

