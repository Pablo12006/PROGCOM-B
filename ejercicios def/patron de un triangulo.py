def mostrar_triangulo_comprension(filas):
  
    for i in range(1, filas + 1):
    
        print(' ' * (filas - i) + '*' * (2 * i - 1))

def generar_triangulo_comprension():
    while True:
      
        filas = int(input("Ingrese el número de filas para el triángulo: "))
        
        
        mostrar_triangulo_comprension(filas)
        

        continuar = input("¿Desea generar otro triángulo? (s/n): ").lower()
        if continuar != 's':
            break


generar_triangulo_comprension()










def mostrar_triangulo_lambda(filas):
    for i in range(1, filas + 1):
    
        generar_fila = lambda i: ' ' * (filas - i) + '*' * (2 * i - 1)
 
        print(generar_fila(i))

def generar_triangulo_lambda():
    while True:
      
        filas = int(input("Ingrese el número de filas para el triángulo: "))
        
     
        mostrar_triangulo_lambda(filas)
        
    
        continuar = input("¿Desea generar otro triángulo? (s/n): ").lower()
        if continuar != 's':
            break


generar_triangulo_lambda()

