distancia_km = int(input("Dime la distancia"))
velocidad_kmh = int(input("Dime la velocidad")) 
tiempo_horas = distancia_km / velocidad_kmh
tiempo_dias = tiempo_horas / 24
print(f"Tardarías {tiempo_dias} días en llegar.")