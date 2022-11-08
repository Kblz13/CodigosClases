def sumaImparesPares(lista1,lista2):
    #validar numeros en lista
    for numeros in lista2:
        if isinstance(numeros,int)==False:#si el numero no es un entero
            return "La lista debe contener solo numeros enteros"
    for numero in lista1:
        if isinstance(numero,int):
            pass
        else:
            return "La lista debe ser de numeros enteros"
    if isinstance(lista1,list) and isinstance(lista2,list):
        if lista1==[] and lista2==[]:
            return []
        else:
            return (sumaux(lista1,lista2))
def sumaux(lista1,lista2):
    par=0
    impar=0
    resultado=[]
    indice=0
    for elemento in lista1:
        indice+=1
        if indice%2==0:
            par+=elemento
        else:
            impar+=elemento
    indice=0
    for elemento in lista2:
        indice+=1
        if indice%2==0:
            par+=elemento
        else:
            impar+=elemento
    resultado=[par,impar]
    return resultado
