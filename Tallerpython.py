import math

#Convertir de Grados a Radianes(Digitando Grados)
g = int(input("Ingrese sus grados a convertir"))
r = math.pi / 3

print(f"Sus grados {g} a grados radianes son: math.radians(g)")

#Pedir el precio de un producto y calcular IVA 21%
p = float(input("Ingrese el precio de un producto"))
iva = (p * 0.21)
ptotal = p + iva

print(f"El precio total de su producto incluyendo el IVA es: {ptotal}")

#Indice de masa muscular
a = float(input("Ingresa tu peso en kilogramos"))
b = float(input("Ingresa tu estatura en metro"))

print("Su indice de masa corporal es: ",a/(b*b))

#Declarar dos variables tipo int X y Y
x = int(input("Digite el primer valor: "))
y = int(input("Digite el segundo valor: "))
n = int(input("Digite el tercer valor: "))
m = int(input("Digite el cuarto valor: "))

print("El valor de x es: " , x , "\n El valor de y es: " , y , "\n El valor de N es: " , n , "\n El valor de M es: " , m)
print("La suma x+y es: ",(x+y),"\n La resta  x-y es: ",(x-y),"\n La multiplicacion  x*y es: ",(x*y),"\n La division x/y es: ",(x/y),"\n El residuo x%y es: ",(x%y))
print("La suma x+N es: ",(x+n),"\n La division y/M es: ",(y/m),"\n El residuo y%M es: ",(x%y))
print("El doble de x es: ",(x*2),"\n El doble de y es: ",(y*2),"\n El doble de N es: ",(n*2),"\n El doble de M es: ",(m*2))
print("La suma x+y+N+M es: ",(x+y+n+m),"\n La multiplicacion x*y*N*M es: ",(x*y*n*m))


#de Km/h a m/s
a = float(input("Digita la velocidad en Km/h: "))
p = a/3,6
print("La velocidad " , a , " Km/h es igual a: ",p, " m/s")

#Calcular Areas
d = int(input("Digita el caracter dependiendo de la figura a la cual le quieras encontrar el area, '1' Circulo, '2' Triangulo o '3' Cuadrado: "))
if d ==1:
    r = float(input("Ingrese el radio: "))
    ar= (math.pi * math.pow(r, 2))
   
    print(f"El area de su circulo es: {str(ar)}")
    
elif d == 2:
    q = float(input("Digite la base del Triangulo: "))
    h = float(input("Digite la altura del Triangulo: "))
    ac = (q * h)/2
    
    print(f"El area de su Triangulo es: {str(ac)}")

elif d == 3:
    z = int(input("Digite el lado de un cuadrado: "))
    acu = math.pow(z,2)

    print(f"El area de su cuadrado es: {str(acu)}")

else:

    print("Caracter incorrecto, Ingrese uno nuevo")






















    
