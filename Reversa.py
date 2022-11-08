"""

"""
def reversa(texto):
    reversa=""
    if isinstance(texto,str):
        for elemento in texto:
            reversa=elemento+reversa
        return reversa
    if isinstance(texto,int):
        numero=0
        while texto>0:  
            numero = 10*numero+texto % 10#
            texto //= 10
        return numero
    else:
        return "El texto debe ser un string o un numero entero"
def reversarecursion(texto,numero=0):
    if isinstance(texto,str):
        if texto=="":
            return ""
        else:
            return reversarecursion(texto[1:])+texto[0]
    if isinstance(texto,int):
        if texto==0:
            return numero
        else:
            numero = 10*numero+texto % 10#agarra el ultimo numero de la variable texto y lo agrega a la variable numero multiplicado por 10 para subar el ultimo numero
            return reversarecursion(texto//10,numero)
    else:
        return "El texto debe ser un string o un numero entero"

print(reversarecursion(1234))

