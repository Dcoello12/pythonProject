import pandas as pd

def inici():
    print("*********************************************")
    print("********* Hola Mundo! SOY DANI **************")
    print("*********************************************")

#Sobreescibre el contenido de un fichero, si no existe lo crea i inserta el contenido#

def fileWrite(fname):
    f = open(fname, "w")
    str = input("Introdueix el teu text: "[:100])
    f.write(str)
    f.close()
#________________________________________________________#

#Añadir texto al final del fichero#
def fileadd(fname):
    f = open(fname, "a")
    str = input("Introdueix el teu text: "[:100])
    f.write(str)
    f.close()
#________________________________________________________#

#Cambiar nombre#
def rename():
    try:
        import os
        new_name = input("Escriu el nou nom del fitxer: ")
        if os.path.exists("files/text.txt"):
            os.rename("files/text.txt", "files/" + new_name)
        else:
            print("El fitxer no existeix")
    finally:
        print("S'ha cambiat el nom correctament.")
#________________________________________________________#

#Crear un fixero pidiendo nombre

def new_file():
    name_file = input("Escriu el nom del fitxer: ")
    f = open("files/" + name_file, "w")
    f.close()
#________________________________________________________#

#Mostrar el contenido de un fichero#

def mostrar():
    name_file = input("Com es diu el fitxer? ")
    f = open("files/" + name_file, "r")
    print(f.read())
    f.close()

#________________________________________________________#

#Main menu#

def menu():
    option = 0
    while True:
        print("""
            Dime, ¿qué quieres hacer?

            1) Crear un fitxer
            2) Mostrar el contingut d'un fitxer
            3) Modificar el contingut d'un fitxer
            4) Sortir
            """)
        option = int(input("Elige una opción: "))

        if option == 1:
            new_file()
            print("Se ha creado correctamente en la carpeta files.")
        elif option == 2:
            mostrar()
        elif option == 3:
            name_file = input("Com es diu el fitxer? ")
            fileWrite("files/" + name_file)
        elif option == 4:
            break
        else:
            print("Opción Incorrecta")
        break
#________________________________________________________#
def taula():
    size = int(input("Quants videos vols intruduir? "))
    for i in range(size):
        dict = {
        "identificador": input("Introdueix el ID: "),
        "grup_cantant": input("Introdueix el grup o el cantant:"),
        "Nom_canço": input("Introdueix el nom de la cançó: "),
        "data_publicació": input("Data de la publicació: ") ,
        "nombre_visualitzacions": int(input("Nombre de visualitzacions: "))
        }
        i = i + 1

    print(dict)
#________________________________________________________#

def taula():
    size = int(input("Quants videos vols introduir? "))
    id_array = []
    cantant_grup_array = []
    nom_canço_array = []
    data_publi_array = []
    n_visualització_array = []

    for i in range(size):
        id = int(input("Introdueix el ID: "))
        id_array.append(id)
        cantant_grup = input("Introdueix el grup o el cantant: ")
        cantant_grup_array.append(cantant_grup)
        nom_canço = input("Introdueix el nom de la cançó: ")
        nom_canço_array.append(nom_canço)
        data_publi = input("Data de la publicació: ")
        data_publi_array.append(data_publi)
        n_visualització = int(input("Nombre de visualitzacions: "))
        n_visualització_array.append(n_visualització)

        dic = {
            'id': id_array,
            'cantant_group': cantant_grup_array,
            'nom_canço': nom_canço_array,
            'data_publi': data_publi_array,
            'n_visualització': n_visualització_array
        }
    ordenar = int(input("Per quina columna vols ordenar?""\n"
                        
                            "1) ID""\n"
                            "2) Cantant_group""\n"
                            "3) Nom_Canço""\n"
                            "4) data_publi""\n"
                            "5) n_visualització""\n"
                        
                        " "))
    if ordenar == 1:
        ordenar = id_array
    elif ordenar == 2:
        ordenar = cantant_grup_array
    elif ordenar == 3:
        ordenar = nom_canço_array
    elif ordenar == 4:
        ordenar = data_publi_array
    elif ordenar == 5:
        ordenar = n_visualització_array
    else:
        print("Opció incorrecta!")

    print(pd.DataFrame(dic, index=[ordenar]))