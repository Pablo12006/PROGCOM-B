import ast

def analizar_codigo_python(codigo):
    errores = []
    try:
        tree = ast.parse(codigo)
        
        # Buscar variables no usadas
        nombres_usados = set()
        nombres_declarados = set()

        for nodo in ast.walk(tree):
            if isinstance(nodo, ast.Name):
                if isinstance(nodo.ctx, ast.Load):
                    nombres_usados.add(nodo.id)
                elif isinstance(nodo.ctx, ast.Store):
                    nombres_declarados.add(nodo.id)

        no_usadas = nombres_declarados - nombres_usados
        for var in no_usadas:
            errores.append(f"⚠️ La variable '{var}' está declarada pero no se usa.")

    except SyntaxError as e:
        errores.append(f"❌ Error de sintaxis en línea {e.lineno}: {e.msg}")

    return errores if errores else ["✅ No se encontraron errores."]

# Prueba con código incorrecto
codigo_prueba = '''
def suma(a, b):
    resultado = a + b   
    x = 10             
    if a > b        
        print("A es mayor") 
    else:
        print("B es mayor") 


'''
errores = analizar_codigo_python(codigo_prueba)

print("\nErrores detectados:")
for e in errores:
    print("- " + e)




