# Debug mode
debug = False


'''

	1.- READING THE ARGUMENTS

	Leemos el nombre del fichero pasado por linea de comandos
	junto con el nombre del pdf a generar

'''
# Mensaje informativo
print('1.- Reading the arguments')

# Leemos los nombres
import sys

# Comprobamos que el numero de los argumentos es correcto
if len(sys.argv) != 3:
	print('Debe hacer un uso correcto de los argumentos a través de la linea de comandos')
	print('Debe usar dos argumentos:')
	print('\t- Nombre del fichero de texto a convertir (con extension)')
	print('\t- Nombre del archivo pdf que desea obtener (con extension)')
	print('\nEjemplo de uso:')
	print('[\tpython3 run.py input.txt output.pdf\t]')
	exit()

# Archivo input
input_name = sys.argv[1]
if debug == True: print('Nombre del fichero a convertir: ', input_name)
# Archivo output
output_name = sys.argv[2]
if debug == True: print('Nombre del PDF a generar: ', output_name)

# Abrimos el fichero
f = open(input_name)



'''

	2.- CREACIÓN DE LA PORTADA

	Se crea la portada usando el nombre del fichero de entrada .txt

'''
# Mensaje informativo
print('2.- Creacion de la portada')

# Quitamos del nombre de entrada la extension
input_name = input_name[:-4] # Recortamos los cuatro ultimos caracteres ".txt"
if debug == True : print('El archivo sin extension es: ', input_name)

# Creamos el canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

c = canvas.Canvas(output_name)
# Tamano de un A4
A4_width = 595.2755905511812  # Tamano horizontal de un A4
A4_height = 841.8897637795277 # Tamano vertical de un A4

# Disenamos la portada
c.setFont('Times-Roman', 32)
text_len = c.stringWidth(input_name, 'Times-Roman', 32)
c.drawString((A4_width/2)-(text_len/2), A4_height-350, input_name)
c.showPage()



'''

	3.- GENERAMOS EL RESTO DE PÁGINAS DE NUESTRO DOCUMENTO

'''
# Cualidades de nuestro documento
rightMargin = 72
leftMargin = 72
topMargin = 72
bottomMargin = 50

font = 'Helvetica'
font_bold = 'Helvetica-Bold'
font_size = 12
c.setFont(font, font_size)

salto_linea = 13

# Funcion a usar para escribir las lienas
from writeLine import writeLine

# De momento nos limitaremos a copiar el contenido pagina a pagina sin mas
longitud_restante = A4_height-topMargin
for linea in f:
	# Escribimos la linea usando la funcion auxiliar
	longitud_restante = writeLine(c, linea, rightMargin, leftMargin, topMargin, bottomMargin, font, font_bold, font_size, salto_linea, longitud_restante, A4_width, A4_height)
	if debug == False: print('\t\t+ Longitud restante: ',longitud_restante)
	# Comprobamos que aun la pagina tenga sitio
	if(longitud_restante <= bottomMargin): # Si ya hemos completado una pagina
		longitud_restante = A4_height - salto_linea # Reseteamos el contador para una nueva linea
		c.showPage() # Pasamos la pagina


'''

	X.- FINALIZAMOS LA CREACION DEL PDF

	X.1.- Finalizamos la creación del PDF
	X.2.- Abrimos automaticamente el PDF

'''
# Mensaje informativo
print('X.- Pdf creado correctamente')

# Guardamos el documento
c.save()

# Abrimos el archivo pfdcon "evince"
import os
os.system('evince '+output_name)
