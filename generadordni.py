
#!/usr/bin/env python

#Generador DNI

import random
import string


#Generador del número de DNI

def randNum(num):

	return "".join(random.choice(string.digits) for t in range(8))


#Generador de letra en base al número generado

def dni(letra):

	seq = 'TRWAGMYFPDXBNJZSQVHLCKE'
	numero=randNum(letra)
	
	return numero + seq[int(numero) % 23] + "\n"


#Escritura del archivo

with open("dni.txt","w") as f:
	for i in range(int(input('\nNumero de DNIs a generar: '))):
		f.write(dni(i))
f.closed
