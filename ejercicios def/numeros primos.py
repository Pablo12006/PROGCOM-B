def es_primo_comprension(numero):
    if numero <= 1:
        return False
    

    divisores = [i for i in range(2, numero) if numero % i == 0]
    

    return len(divisores) == 0

def verificar_primo_comprension():
    while True:

        numero = int(input("Ingrese un número: "))
        
    
        if es_primo_comprension(numero):
            print(f"{numero} es un número primo.")
        else:
            print(f"{numero} no es un número primo.")
        
        continuar = input("¿Desea verificar otro número? (s/n): ").lower()
        if continuar != 's':
            break


verificar_primo_comprension()











def es_primo_lambda(numero):
    if numero <= 1:
        return False
    
  
    divisores = list(filter(lambda x: numero % x == 0, range(2, numero)))

    return len(divisores) == 0

def verificar_primo_lambda():
    while True:
        numero = int(input("Ingrese un número: "))
        
    
        if es_primo_lambda(numero):
            print(f"{numero} es un número primo.")
        else:
            print(f"{numero} no es un número primo.")
        
        continuar = input("¿Desea verificar otro número? (s/n): ").lower()
        if continuar != 's':
            break


verificar_primo_lambda()
