distancia_km = 225000000
for velocidad_kmh in range(10000, 50001, 10000):
    tiempo_horas = distancia_km / velocidad_kmh
    tiempo_dias = tiempo_horas / 24
    print(f'A {velocidad_kmh} km/h se tarda {tiempo_dias} dias en llegar a Marte')