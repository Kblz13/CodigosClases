def largolista(lista):
    if isinstance(lista,list):
        if lista==[]:
            return 0
        else:
            return 1+largolista(lista[1:])
    else:
        return "La lista debe ser una lista"
