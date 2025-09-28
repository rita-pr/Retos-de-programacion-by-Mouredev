# ==========================================================================
# Reto 1 - Fizz Buzz
# September 27, 2025
# ==========================================================================

# ==========================================================================
 # Escribe un programa que muestre por consola (con un print) los
 # números de 1 a 100 (ambos incluidos y con un salto de línea entre
 # cada impresión), sustituyendo los siguientes:
 # - Múltiplos de 3 por la palabra "fizz".
 # - Múltiplos de 5 por la palabra "buzz".
 # - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
# ==========================================================================

# Nota: se trabajará para un caso generalizado, con límites "n" y "m"

# Recordar que las funciones van hasta arriba
def fizz_buzz (n:int, m:int):    
    """ Imprime los números de n hasta m, y cambio por fizzbuzz """

    for valor in range (n,m+1):
        #print(valor) aquí sería para probar que imprima los números que necesito
        if valor % 3 == 0 and valor % 5 == 0:
            print("fizzbuzz")
        elif valor % 3 == 0:
            print("fizz")
        elif valor % 5 == 0:
            print("buzz")
        else:
            print(valor)
            # El print va con else, porque no queremos que siempre imprima, 
            # sino que, hasta que validemos que no se hayan cumplido 
            # las condiciones anteriores

n = int(input("Ingrese límite inferior: "))
m = int(input("Ingrese límite superior: "))

fizz_buzz(n,m)
# llamar la función quedó abajo se pone abajo porque si
# estuviera arriba, aún no existen n y m


# Auto feedback (puntos de mejora)
# - Recordar la diferencia entre print y return, y el efecto según la identación que tienen.
# - Uso del else.