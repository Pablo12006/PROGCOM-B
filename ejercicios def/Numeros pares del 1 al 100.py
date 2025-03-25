def mostrar_pares_comprension():

    pares = [numero for numero in range(1, 101) if numero % 2 == 0]
    
 
    print("Números pares del 1 al 100:")
    print(pares)

mostrar_pares_comprension()



def mostrar_pares_lambda():
    
    pares = list(filter(lambda x: x % 2 == 0, range(1, 101)))
    
  
    print("Números pares del 1 al 100:")
    print(pares)

mostrar_pares_lambda()
