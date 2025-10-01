# ==========================================================================
# Reto 4 - Vocal más común
# September 30, 2025
# ==========================================================================

# ==========================================================================
# Crea un función que reciba un texto y retorne la vocal que
# más veces se repita.
#   - Ten cuidado con algunos casos especiales.
#   - Si no hay vocales podrá devolver vacío.
# ==========================================================================

def vocal_comun (cadena):
    for vocal in vocales:
        conteo = cadena.count(vocal)
    return max(conteo)


cadena = input("Ingrese cadena: ")

minuscula = list(cadena.strip().lower())
vocales = ["a", "e", "i", "o", "u"]

print(vocal_comun(cadena))
