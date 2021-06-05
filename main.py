def validar(a):
	"""
	Comprueba que la entrada es un número y que se encuentra en el rango correcto
	"""
	try:
		a = int(a)
	except:
		return False
	else:
		if a < 0 or a > 440:
			return False
		else:
			return True


def ubicar(a, b):
	"""
	Localiza el puerto físicamente
	"""
	columna = ((a - b[0]) // b[2]) + 1
	fila = ((a - b[0])% b[2]) + 1
	
	return [b[3], b[4], columna, fila]


def formatear(a):
	"""
	Devuelve una cadena en el formato W/X/Y/Z, donde W y X son respectivamente la columna y la fila de la tarjeta mientras que Y y Z son respectivamente la columna y la fila del puerto
	"""
	cadena = ""
	
	for i in range(len(a)):
		cadena += str(a[i])
		if i < 3:
			cadena += "/"
		
	return cadena


# A continuación se definen los datos de las tarjetas de un MDF. No son los datos reales que utilicé en este proyecto.

# Cada lista tiene el número del primer y último puerto, la cantidad de filas de la tarjeta y la columna y la fila donde se encuentra la tarjeta. Todo en ese orden.
T1 = [0, 40, 8, 1, 1]
T2 = [41, 80, 8, 1, 2]
T3 = [81, 130, 10, 1, 3]
T4 = [131, 180, 8, 1, 4]
T5 = [181, 220, 8, 1, 5]
T6 = [221, 270, 10, 2, 1]
T7 = [271, 310, 8, 2, 2]
T8 = [311, 350, 8, 2, 3]
T9 = [351, 400, 10, 2, 4]
T10 = [401, 440, 8, 2, 5]

# Agrupar todos los datos de las tarjetas en una sola lista
tarjetas = [T1, T2, T3, T4, T5, T6, T7, T8, T9, T10]

# Ciclo infinito
while True:
	puerto = input("> ")
	
	# Validar puerto
	if not validar(puerto):
		print("No has introducido un valor válido. Vuelve a intentarlo.")
	else:
		puerto = int(puerto)
		
		# Buscar la posicion del puerto
		for i in tarjetas:
			if puerto >= i[0] and puerto <= i[1]:
				posicion = ubicar(puerto, i)
		
		# Formatear el texto a imprimir
		posicion = formatear(posicion)
		print(posicion)