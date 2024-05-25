#Aaron Gabriel Leale Xamena A112 23/05/2024 
from funciones_calculadora import *

while True:

    valor1 = obtener_numero("Ingrese un número: ")
    valor2 = obtener_numero("Ingrese otro número: ")

    eleccion = input(
                    "sumar          (" + str(valor1) + "+" + str(valor2) + "):\n"
                    "restar         (" + str(valor1) + "-" + str(valor2) + "):\n"
                    "multiplicar    (" + str(valor1) + "*" + str(valor2) + "):\n"
                    "dividir        (" + str(valor1) + "/" + str(valor2) + "):\n"
                    "factorizar   (" + "!" + str(valor1) + ",!" + str(valor2) + "):\n"
                    "calcular todas      :\n"
                    "salir               :\n"
                    "\nelija una opcion: "
                    )
    
    if eleccion == "salir" or eleccion == "Salir":
        break

    if eleccion == "sumar" or eleccion == "Sumar":
        mostrar_valores(valor1,valor2)
        sumar_numeros(valor1,valor2)

    elif eleccion == "restar" or eleccion == "Restar":
        mostrar_valores(valor1,valor2)
        restar_numeros(valor1,valor2)

    elif eleccion == "dividir" or eleccion == "Dividir":
        mostrar_valores(valor1,valor2)
        dividir_numeros(valor1,valor2)

    elif eleccion == "multiplicar" or eleccion == "Multiplicar":
        mostrar_valores(valor1,valor2)
        multiplicar_numeros(valor1,valor2)

    elif eleccion == "factorizar" or eleccion == "Factorizar":
        mostrar_valores(valor1,valor2)
        print("el factorial del primer numero: "+str(factorizar(valor1)))
        print("el factorial del segundo numero: "+str(factorizar(valor2)))

    if eleccion == "calcular todas" or eleccion == "Calcular todas":
        mostrar_valores(valor1,valor2)
        sumar_numeros(valor1,valor2)
        restar_numeros(valor1,valor2)
        dividir_numeros(valor1,valor2)
        multiplicar_numeros(valor1,valor2)
        print("el factorial del primer numero: "+str(factorizar(valor1)))
        print("el factorial del segundo numero: "+str(factorizar(valor2)))
    

    continuar = input("\ndesea hacer otra operacion?: ")
    if continuar == "no":
        break



