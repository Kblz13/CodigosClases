def convertirbinario(numero):
    if isinstance(numero,int):
        if numero==0:
            return 0
        else:
            return numero%2+10*convertirbinario(numero//2)
    else:
        return "El numero debe ser un entero"
