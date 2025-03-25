import random

def adivinar_color_comprension():

    colores = ["rojo", "azul", "verde", "amarillo", "naranja", "rosa", "morado", "negro", "blanco", "gris"]
    
    
    print("Colores disponibles para adivinar:")
    print(", ".join([color for color in colores]))
    print()  


    color_aleatorio = random.choice(colores)
 
    intentos = 0
    while intentos < 3:  
        adivinanza = input("Adivina el color: ")

      
        es_correcto = [True for color in [color_aleatorio] if adivinanza == color]

        if es_correcto:  
            print(f"¡Correcto! El color era {color_aleatorio}. Lo adivinaste en {intentos + 1} intentos.")
            break
        else:
            print("Intenta de nuevo.")
        
        intentos += 1

    if intentos == 3:
        print(f"Lo siento, perdiste. El color era {color_aleatorio}.")

adivinar_color_comprension()







import random

def adivinar_color_lambda():
   
    colores = ["rojo", "azul", "verde", "amarillo", "naranja", "rosa", "morado", "negro", "blanco", "gris"]

    print("Colores disponibles para adivinar:")
    print(", ".join(colores))
    print()  

    color_aleatorio = random.choice(colores)
    
    
    intentos = 0
    while intentos < 3:  
        adivinanza = input("Adivina el color: ")

       
        es_correcto = adivinanza == color_aleatorio


        if es_correcto:
            print(f"¡Correcto! El color era {color_aleatorio}. Lo adivinaste en {intentos + 1} intentos.")
            break
        else:
            print("Intenta de nuevo.")
        
        intentos += 1
        
    if intentos == 3:
        print(f"Lo siento, perdiste. El color era {color_aleatorio}.")

adivinar_color_lambda()
