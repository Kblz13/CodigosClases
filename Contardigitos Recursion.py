"""
Nombre de la función:contar digito
entradas:un número y su indice
"""
def ContarDigitos(num):
    if isinstance(num,int)and num>=0:
        if num==0:
            return 0
        else:
            return 1 + ContarDigitos(num//10)
    else:
        return "El número debe de ser entero y positivo"""
