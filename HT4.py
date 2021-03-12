
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
def mostrar_tabla_fruas():
    print('fruta - precio por Kg')
    for a in tabla_de_frutas:
        print(a + ' - '+ str(tabla_de_frutas[a]))

def pedir_fruta():
    seguir = True
    while(seguir):
        mostrar_tabla_fruas()
        nom_fruta = input('Que fruta desea?')
        nom_fruta = nom_fruta.lower()
        if (nom_fruta in tabla_de_frutas_minusculas):
            cant_fruta = input("Cuantos kilos de esta fruta desea?")
            cant_f = float(cant_fruta)
            total = round(cant_f*tabla_de_frutas_minusculas[nom_fruta],2)
            print("Costo total por "+str(cant_f)+"Kg de "+str(nom_fruta)+" = "+str(total))
        else:
            print('Esta fruta no esta disponible :C')

        continuar = input('Desea continuar evaluando? y/n')
        continuar = continuar.lower()
        if(continuar=='n'):
            return

def tabla_de_multiplicar():
    num = input("De que numero entre el 1 al 10 desea la tabla de multiplicar?")
    try:
        num = int(num)
        if num<0 or num>10:
            print('Solo se permiten numeros del 1 al 10')
            return
    except:
        print('Ese no era un numero valido')
    content = "Tabla del "+str(num)
    i=0
    while i <= 10:
        content+="\n"+str(num)+" x "+str(i)+" = "+str(num*i)
        i=i+1
    print(content)
    f = open("tabla-"+str(num)+".txt", "w")
    f.write(content)
    f.close()
    print("Gracias, feliz dia")

pedir_fruta()
tabla_de_multiplicar()





