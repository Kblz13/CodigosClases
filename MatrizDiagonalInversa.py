#Entrada: una matriz
#Salida: la matriz con sus diagonales invertidas
#restricciones: debe ser una matriz
def matrizDiagonalInversa(matriz,resultadofinal=[],indice=0):
    if isinstance(matriz,list) :
        if  largolista(resultadofinal)==3:
            return resultadofinal
        else:
            return matrizDiagonalInversa(matriz[1:],resultadofinal+[matriz[0][indice]],indice+1)
    else:
        return "La matriz debe ser una lista y no debe estar vacia"
