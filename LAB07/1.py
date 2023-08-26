persona = {
 'first_name': 'Edem',
 'last_name': 'Terraza',
 'age': 31,
 'country': 'Peru',
 'is_married': True,
 'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
 'address': {
 'street': 'Space street',
 'zipcode': '02210'
 }
}

#a) 
if 'skills' in persona:
    habilidades = persona['skills']
    if len(habilidades) >= 3:
        habilidad_media = habilidades[len(habilidades) // 2]
        print("Habilidad del medio:", habilidad_media)

#b)
if 'skills' in persona and 'Python' in persona['skills']:
    print("Tiene la habilidad 'Python'.")

#c) 
if 'skills' in persona:
    habilidades = persona['skills']
    if set(habilidades) == {'JavaScript', 'React'}:
        print("Él es un desarrollador frontend")
    elif set(habilidades) == {'Node', 'Python', 'MongoDB'}:
        print("Él es un desarrollador backend")
    elif set(habilidades) == {'React', 'Node', 'MongoDB'}:
        print("Él es un desarrollador fullstack")
    else:
        print("Título desconocido")
