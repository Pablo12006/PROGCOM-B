def es_numero_armstrong_comprension(num):

    digitos = [int(d) for d in str(num)]
    
    n_digitos = len(digitos)
   
    suma = sum([d ** n_digitos for d in digitos])
    return suma == num

def encontrar_numeros_armstrong_comprension(n):
   
    return [i for i in range(1, n+1) if es_numero_armstrong_comprension(i)]

def mostrar_numeros_armstrong_comprension():
    while True:
     
        n = int(input("Ingrese un número n: "))
        
       
        numeros_armstrong = encontrar_numeros_armstrong_comprension(n)
        print(f"Los números Armstrong hasta {n} son: {numeros_armstrong}")
        
       
        continuar = input("¿Desea encontrar más números Armstrong? (s/n): ").lower()
        if continuar != 's':
            break


mostrar_numeros_armstrong_comprension()





def es_numero_armstrong_lambda(num):
    
    digitos = [int(d) for d in str(num)]
   
    n_digitos = len(digitos)
    
    suma = sum(map(lambda d: d ** n_digitos, digitos))
    return suma == num

def encontrar_numeros_armstrong_lambda(n):
    
    return list(filter(es_numero_armstrong_lambda, range(1, n+1)))

def mostrar_numeros_armstrong_lambda():
    while True:
       
        n = int(input("Ingrese un número n: "))
        
       
        numeros_armstrong = encontrar_numeros_armstrong_lambda(n)
        print(f"Los números Armstrong hasta {n} son: {numeros_armstrong}")
        
        continuar = input("¿Desea encontrar más números Armstrong? (s/n): ").lower()
        if continuar != 's':
            break


mostrar_numeros_armstrong_lambda()
