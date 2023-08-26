from Countries_data import countries
from collections import Counter

def paises_mas_poblados(num_paises):
    paises_mas_poblados_mundo = sorted(countries, key=lambda x: x['population'], reverse=True)[:20]
    return paises_mas_poblados_mundo


def idiomas_mas_hablados(num_idiomas):
    contador_leguajes = Counter()
    for country in countries:
        lenguajes = country['languages']
        contador_leguajes.update(lenguajes)
    lenguajes_mas_top = contador_leguajes.most_common(num_idiomas) 
    return lenguajes_mas_top


#a
top_idiomas = idiomas_mas_hablados(20)
print("Los 20 idiomas más hablados del mundo son:")
for language, count in top_idiomas:
    print(f"{language}: {count} países")

#b
paises_mas_poblados = paises_mas_poblados(20)
print("Los paises más poblados son: ")
for index, country in enumerate(paises_mas_poblados, start=1):
    print(f"{index}. {country['name']}: {country['population']}")