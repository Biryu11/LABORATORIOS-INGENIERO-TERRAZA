from Countries_data import countries


#a
todos_los_lenguajes = set()
for country in countries:
    for lenguaje in country["languages"]:
        todos_los_lenguajes.add(lenguaje)

print(f"Numero total de lenguajes: {len(todos_los_lenguajes)}")






#b
conteo_lenguajes = {}
for country in countries:
    for lenguaje in country["languages"]:
        if lenguaje in conteo_lenguajes:
            conteo_lenguajes[lenguaje] += 1
        else:
            conteo_lenguajes[lenguaje] = 1

lenguas_sorteadas = sorted(conteo_lenguajes.items(), key=lambda x: x[1], reverse=True)
top_lenguajes = lenguas_sorteadas[:10]

print("Los 10 idiomas màs hablados:")
for lang, count in top_lenguajes:
    print(f"{lang}: {count} countries")





#c
paises_sorteados = sorted(countries, key=lambda x: x["population"], reverse=True)
top_paises_populares = paises_sorteados[:10]

print("LOs 10 paises mas populares:")
for country in top_paises_populares:
    print(f"{country['name']}: {country['population']} people")