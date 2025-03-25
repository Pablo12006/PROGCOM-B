def es_numero_perfecto_comprension(num):
  
    divisores = [i for i in range(1, num) if num % i == 0]
   
    return sum(divisores) == num

def encontrar_numeros_perfectos_comprension(n):
  
    numeros_perfectos = [i for i in range(1, n+1) if es_numero_perfecto_comprension(i)]
    return numeros_perfectos

def mostrar_numeros_perfectos_comprension():
    while True:
       
        n = int(input("Ingrese un número n: "))
        
      
        numeros_perfectos = encontrar_numeros_perfectos_comprension(n)
        print(f"Los números perfectos hasta {n} son: {numeros_perfectos}")
        
        
        continuar = input("¿Desea encontrar más números perfectos? (s/n): ").lower()
        if continuar != 's':
            break


mostrar_numeros_perfectos_comprension()




def es_numero_perfecto_lambda(num):
   
    divisores = list(filter(lambda i: num % i == 0, range(1, num)))
    return sum(divisores) == num

def encontrar_numeros_perfectos_lambda(n):

    return list(filter(es_numero_perfecto_lambda, range(1, n+1)))

def mostrar_numeros_perfectos_lambda():
    while True:

        n = int(input("Ingrese un número n: "))
        
        
        numeros_perfectos = encontrar_numeros_perfectos_lambda(n)
        print(f"Los números perfectos hasta {n} son: {numeros_perfectos}")
        
        continuar = input("¿Desea encontrar más números perfectos? (s/n): ").lower()
        if continuar != 's':
            break


mostrar_numeros_perfectos_lambda()

