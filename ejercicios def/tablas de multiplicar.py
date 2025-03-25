def mostrar_tablas_comprension():
 
    for i in range(1, 11):
        tabla = [f"{i} x {j} = {i * j}" for j in range(1, 11)]
        
       
        print("\n".join(tabla))
        print("-" * 20)  


mostrar_tablas_comprension()



def mostrar_tablas_lambda():
  
    for i in range(1, 11):
        
        tabla = list(map(lambda j: f"{i} x {j} = {i * j}", range(1, 11)))
        
       
        print("\n".join(tabla))
        print("-" * 20) 


mostrar_tablas_lambda()
