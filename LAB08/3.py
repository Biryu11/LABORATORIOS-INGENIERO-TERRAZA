import random


minusculas = 'abcdefjhijklmnñoprstuvwxyz'
mayusculas = minusculas.upper()

nume = '1234567890'
caracacteresEspeciales = '!@#$%&/'


caracteresTotales = 8
totalcaracteres= minusculas+mayusculas+nume+caracacteresEspeciales
contraseñaRandom = random.sample(totalcaracteres,caracteresTotales)
contraseña = ''.join(contraseñaRandom)
print(f"la contraseña creada es: {contraseña}")