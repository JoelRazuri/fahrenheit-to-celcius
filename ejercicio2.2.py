""" 
Escribir un programa que convierta un valor dado en grados Fahrenheit a grados
Celsius. Recordar que la fórmula para la conversión es: 𝐹 = 9/5𝐶 + 32
""" 

print("------------------------------")
print("Convertidor de Fahrenhiet a Celsius")

grados_f = float(input("Ingrese una temperatura:"))

grados_c = (grados_f - 32 ) * 5/9

print("")
print(f"{grados_f:.2f} º Fahrenhiet son igual a {grados_c:.2f} º Celsius")

