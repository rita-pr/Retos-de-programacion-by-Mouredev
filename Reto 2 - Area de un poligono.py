# ==========================================================================
# Reto 2 - Área de un polígono
# September 28, 2025
# ==========================================================================

# ==========================================================================
# Crea una única función (importante que sólo sea una) que sea capaz
# de calcular y retornar el área de un polígono.
# - La función recibirá por parámetro sólo UN polígono a la vez.
# - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
# - Imprime el cálculo del área de un polígono de cada tipo.
# ==========================================================================

def area_poligono (poligono, base, altura):
    if poligono == "T":
        area = (1/2) * base * altura
        print(f"El área es de: {area}")
    elif poligono == "C" or poligono == "R":
        area = base * altura
        print(f"El área es de: {area}")

poligono = input("Seleccionar polígono:\n[T]riángulo, [C]uadrado, [R]ectángulo: ")
base = float(input("Ingresar base: "))
altura = float(input("Ingresar altura: "))

area_poligono(poligono, base, altura)


# Auto feedback: otra vez problema con diferenciar cuándo usar elif y cuándo else, mejor si else queda
# para cuando no se coloque la condición (aunque sí se podría, pero es más largo)