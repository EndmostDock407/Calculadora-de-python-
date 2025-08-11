# calculadora en python primer parte

# two input numbers, then adds them together and prints the result

print ("\nCalculadora python, primera parte, Suma de 2 números")
n1= float(input("\nEscribe el primer numero "))
n2= float(input("\nEscribe el segundo numero "))
print(f"\n{n1} + {n2} = {n1+n2}")

input("\nPrimer parte terminada, presiona Enter para continuar...\n")



# calculadora en python segunda parte FEATURES
# Se definen las funciones de cada operación 
# Cada función utiliza valores "a" y "b"


def suma(a, b):                                                                 #--------Take two numbers and subtract the second from the first number.
    print(f"\n{a} + {b} = {a + b}\n")                                           # Toda la operacion junto al resultado

def suma3(a, b, c):                                                             #--------Take 3 numbers and add them together.
    print(f"\n{a} + {b} + {c} = {a + b + c}\n")                                 

def resta(a, b):
    print(f"\n{a} - {b} = {a - b}\n") 

def division(a, b):                                                             #-------Take two numbers and divide the first number by the second number
    if b != 0:                                                                  # El " if " se encarga de que cualquier valor en b mayor a 0 es aceptado
        print(f"\n{a} / {b} = {a / b}\n")
    else:                                                                       # si se elige cero para b, " else " da error ya que no se puede dividir entre 0 
        print (" No se puede dividir entre cero")

def multiplicacion(a, b):                                                       #-------Take two numbers and multiply the two
     print(f"\n{a} / {b} = {a / b}\n") 

def modulo(a ,v):                                                               #-------Take two numbers and perform a modulus operation.
     print(f"\n{a} modulo {b} = {a % b}\n")

def expresion_libre(expr):                                                      #-------Allow users to mix operations with 3 numbers or more
    try:
        resultado = eval(expr)                                                  # Permite escribir una operacion como texto, que será interpretada como operacion
        print(f"\nResultado de la expresión: {expr} = {resultado}\n")
    except Exception as e:
        print(f"\nError en la expresión: {e}\n")


# Se despliega el menú de opciones 
# Se usa una variable, a la que se le asigna un valor " int " que corresponderá a cada función dentro de un menú de opciones


#--------Allow users to choose which operation they want to perform on two numbers

eleccion = int(input("\nCalculadora escrita en python Segunda parte \n\n " \
"Elige lo que quieres hacer  \n\n  " \
"1 Suma \n2 Resta \n3 Division  \n4 Multiplicacion \n5 Modulo  " \
"6 Suma con 3 valores \n7 Operacion combinada \n\n ----->  " ))                     # Por medio del " input" se pide al usuario escribir el valor 
                                                                                    # Para más facilidad, se despliega el menu dentro del " input "
                                                                                    #       y se usa saltos de linea para hacerlo más estético


if eleccion >= 1 and eleccion <= 7:                                                 # Si la elección se encuentra en el menú, lo que es igual a que
    if eleccion == 6:
        a = float(input("\nEscriba el primer valor: "))
        b = float(input("Escriba el segundo valor: "))
        c = float(input("Escriba el tercer valor: "))
        suma3(a, b, c)
    elif eleccion == 7:
        expr = input("\nEscribe la expresión matemática (ej. 2 + 4 - 3 * 2): ")
        expresion_libre(expr)
    else:    
        a=float(input("\nEscriba el primer valor:  "))                              # el valor este dentro del rango 1 y 4, se pediran los valores " a " y " b "
        b=float(input("Escriba el segundo valor:  "))                               # Para ampliar el rango de uso, se transforman los valores a flotante

        if eleccion == 1:                                                           # Si la " eleccion " Esta en el menu, los " if " y " elif " ejecutaran el 
                suma(a, b)                                                          # código que contengan
        elif eleccion == 2:
                resta(a, b)                                                         # Se manda a llamar a las funciones dependiendo de lo elegido
        elif eleccion ==3:
                division(a, b)
        elif eleccion == 4:
                multiplicacion(a, b)
        elif eleccion ==5:
                modulo(a, b)
else:                                                                              # Si " eleccion " no cumple la condicional, manda el mensaje de error
    print( "Opción no disponible")      


# Fin del programa 
