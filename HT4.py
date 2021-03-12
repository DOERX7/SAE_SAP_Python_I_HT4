
tabla_de_frutas={
    'Platano':1.35,
    'Manzana': 0.8,
    'Pera': 0.85,
    'Naranja': 0.7
}
tabla_de_frutas_minusculas={
    'platano':1.35,
    'manzana': 0.8,
    'pera': 0.85,
    'naranja': 0.7
}

def pedir_fruta():
    seguir = True
    while(seguir):
        nom_fruta = input('Que fruta desea?')
        nom_fruta = nom_fruta.lower()
        if (nom_fruta in tabla_de_frutas_minusculas):
            cant_fruta = input("Cuantas de estas frutas desea?")
            cant_f = float(cant_fruta)
            total = round(cant_f*tabla_de_frutas_minusculas[nom_fruta],2)
            print(total)
        else:
            print('Esta fruta no esta disponible :C')

        continuar = input('Desea continuar evaluando? y/n')
        continuar = continuar.lower()
        if(continuar=='n'):
            return

def tabla_de_multiplicar():
    num = input("Que numero desea multiplicar?")
    num = int(num)
    content = "Tabla del "+str(num)+"\n"
    i=0
    while i <= 10:
        content+="\n "+str(num*i)
        i=i+1

    f = open("tabla-n.txt", "w")
    f.write(content)
    f.close()

pedir_fruta()
tabla_de_multiplicar()





