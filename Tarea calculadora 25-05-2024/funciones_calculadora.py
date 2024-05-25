def mostrar_valores(valor1, valor2):
    print("\n") #espacio para no sobrecargar el aspecto del menu
    print("valor 1 : " + str(valor1))
    print("valor 2 : " + str(valor2))
    print("\n") #  ""          ""           ""         ""
    

def obtener_numero(prompt):
    while True:
        try:
            valor = int(input(prompt)) ##verifica que se haya ingresado un numero
            return valor #retorna en caso que si
        except ValueError:#presenta error en caso que no
            print("Por favor, introduzca un número.")

def sumar_numeros(numero_1:int, numero_2:int) -> int: 
    return print("la suma da: " + str(numero_1 + numero_2)) # retorna la suma 
                                                            # no es necesario verificar ya que se hizo al introducir los numeros

def restar_numeros(numero_1:int, numero_2:int)-> int: 
    return print("la resta da: " + str(numero_1 - numero_2)) #retona la resta


def dividir_numeros(numero_1:int, numero_2:int)-> int: 
    if numero_2 != 0:#---------------------------------# verifica que el divisor no sea 0
        resultado = round(numero_1 / numero_2, 3)
        return print(f"La división da: {resultado}") #retorna la division en caso que no lo sea
    else: 
        return print("No es posible dividir por cero") #retorna este mensaje de error en caso que si sea 0


def multiplicar_numeros(numero_1:int, numero_2:int)-> int: 
    return print("la multiplicacion da: " + str(numero_1 * numero_2)) # retorna la multiplicacion


def factorizar(n:int)->int:
    if n < 0:#--------------------------------------------------#verifica que el numero no sea negativo
        return ("No esta definido el factorial de un negativo") #retorna este mensaje en caso que si lo sea
    fact = 1 
    for i in range (2, n + 1):                                  
        fact *= i
    return fact#--------------------------------------------------#retorna el resultado del factoreo
