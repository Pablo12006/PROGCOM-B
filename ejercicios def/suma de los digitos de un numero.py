def suma_digitos_lambda(numero):
  
    return sum(map(lambda x: int(x), str(numero)))

def calcular_suma_lambda():
    while True:
   
        numero = int(input("Ingrese un número: "))
        
      
        resultado = suma_digitos_lambda(numero)
        print(f"La suma de los dígitos de {numero} es: {resultado}")
        
      
        continuar = input("¿Desea calcular otro número? (s/n): ").lower()
        if continuar != 's':
            break


calcular_suma_lambda()








def suma_digitos_comprension(numero):
  
    return sum([int(digit) for digit in str(numero)])

def calcular_suma_comprension():
    while True:

        numero = int(input("Ingrese un número: "))
        

        resultado = suma_digitos_comprension(numero)
        print(f"La suma de los dígitos de {numero} es: {resultado}")
        

        continuar = input("¿Desea calcular otro número? (s/n): ").lower()
        if continuar != 's':
            break


calcular_suma_comprension()
