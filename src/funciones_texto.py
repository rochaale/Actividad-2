def contar_lineas(texto):
    
    return len(texto.split("."))

def contar_palabras(texto):
    return len(texto.split())

def palabras_por_linea(texto):
    total = 0
    resultado = []
    for linea in texto.split("."):
        resultado.append(len(linea.split()))
    return resultado
    
def linea_sobre_promedio(texto):
    resultado = []
    promedio = contar_palabras(texto) / contar_lineas(texto)
    for linea in texto.split("."):
        if len(linea.split()) > promedio:
            resultado.append(linea)
    return resultado

    