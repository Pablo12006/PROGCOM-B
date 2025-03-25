def generar_diamante_comprension(filas):
    
    for i in range(1, filas + 1):
       
        linea = ' ' * (filas - i) + '*' * (2 * i - 1)
        print(linea)

    
    for i in range(filas - 1, 0, -1):
        
        linea = ' ' * (filas - i) + '*' * (2 * i - 1)
        print(linea)

def mostrar_diamante_comprension():
    while True:
       
        filas = int(input("Ingrese el número de filas para la mitad superior del diamante: "))
        
        
        generar_diamante_comprension(filas)
        
        continuar = input("¿Desea generar otro diamante? (s/n): ").lower()
        if continuar != 's':
            break


mostrar_diamante_comprension()






def generar_diamante_lambda(filas):
    
    for i in range(1, filas + 1):
    
        generar_linea = lambda i: ' ' * (filas - i) + '*' * (2 * i - 1)
        print(generar_linea(i))

    
    for i in range(filas - 1, 0, -1):
   
        generar_linea = lambda i: ' ' * (filas - i) + '*' * (2 * i - 1)
        print(generar_linea(i))

def mostrar_diamante_lambda():
    while True:
        
        filas = int(input("Ingrese el número de filas para la mitad superior del diamante: "))
        
       
        generar_diamante_lambda(filas)
        
       
        continuar = input("¿Desea generar otro diamante? (s/n): ").lower()
        if continuar != 's':
            break



mostrar_diamante_lambda()
