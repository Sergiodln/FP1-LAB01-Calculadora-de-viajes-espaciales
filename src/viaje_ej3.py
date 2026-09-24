edad = int(input("Dime tu edad"))
nivel_fisico = int(input("Dime tu nivel físico (de 1 a 10)"))

#Me ha faltado esto:
while (nivel_fisico< 1) or (nivel_fisico>10):
    print("No válido")
    nivel_fisico = int(input("Dime tu nivel físico (de 1 a 10)"))
    if (nivel_fisico>= 1) and (nivel_fisico<=10):
        break
if edad < 18:
    print("Debes ser mayor de edad")
elif nivel_fisico < 5:
    print("Debes estar en mejor forma")
else:
    print("¡Listo para despegar!")