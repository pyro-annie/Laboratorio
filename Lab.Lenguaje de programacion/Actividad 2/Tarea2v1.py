#Primer intento con operaciones matematicas ,pero al darme cuenta no dio 52,si no 51 
# por que python redonde al numero entero mas cercano,al convertir el valor 
# con int() ,se obtiene el valor 52.0 pero python lo tranforma a 51

# Para obtener la parte entera de un número decimal, podemos usar la función int()
numero_decimal = 7.52
parte_entera = int(numero_decimal)
print(f"La parte entera de {numero_decimal} es {parte_entera}")

# Para obtener la parte decimal de un número decimal, podemos restar la parte entera del número original
# y luego multiplicar por 100 para obtenerla como un número entero
parte_decimal = int((numero_decimal - parte_entera) * 100)
print(f"La parte decimal de {numero_decimal} es {parte_decimal}")
