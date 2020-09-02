# Debug mode
debug = False

'''

    0.- Obtenemos y ordenamos las subcarpetas

'''
print('0.- Obtenemos y ordenamos las subcarpetas')

import os
from datetime import datetime

# Obtenemos el listado de subcarpetas a leer

ruta_app = os.getcwd() # Obtain script route
ruta_app = ruta_app + '/Inputs/' # We read the files only desde la carpeta de Inputs
contenido = os.listdir(ruta_app) # Obtaining list of archives and subdirectories

# Ordenamos la lista de contenido de menor a mayor, para guardar los idiomas siempre en el mismo orden
i = 0
while i <= len(contenido):
    j = 0
    for element in contenido:
        if j < (len(contenido)-1):
            pos_1 = contenido[j].find('_')
            pos_2 = contenido[j+1].find('_')

            part_1 = int(contenido[j][:pos_1])
            if debug == True: print(j+1, ' -> ', contenido[j+1], ' -> ',contenido[j+1][:pos_2]) # Debug info
            part_2 = int(contenido[j+1][:pos_2])

            if part_1 > part_2: # We swap their values
                copy = contenido[j+1]
                contenido[j+1] = contenido[j]
                contenido[j] = copy

        j += 1
    i += 1


'''

    1.- Leemos todo el contenido de las subcarpetas

    + Leemos el contenido de las subcarpetas que se encuentran dentro de la carpeta "Inputs"
    + To save the content in a particular order

'''
print('\n1.- Leemos todo el contenido de las subcarpetas')

from os import listdir

# Procesamos el contenido de las subcarpetas
informacion = list()
for elemento in contenido:
    if debug == True: print('\t- Reading folder... ', elemento)
    info = list()
    info.append(elemento)
    # Miramos cada uno de los ficheros
    for file in listdir('Inputs/'+elemento):
        if debug == True: print('\t\t+ Reading file... ',file)
        info.append(file)
        f = open('Inputs/'+elemento+'/'+file, 'r')
        content = list()
        for linea in f:
            content.append(linea)
        if debug == True: print('\t\t+ Content of the file... ', content)
        info.append(content)
        f.close()
    informacion.append(info)


'''

    2.- Creamos PDF con toda la informacion recolectada

'''
print('\n2.- Creamos PDF con toda la informacion recolectada')

# Obtenemos nombre del pdf que se desea generar
import sys
input_name = -1
if len(sys.argv) == 2:
    output_name = sys.argv[1]
    output_name = output_name[:-4] # Quitamos la extension
    print('\t- Nombre del archivo a generar: "',output_name,'""')
else:
    output_name = 'default'
    print('\t- Nombre del archivo a generar: "default.pdf"')


# Creamos PDF
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

c = canvas.Canvas(output_name+'.pdf')

# Tamano de un A4
A4_width = 595.2755905511812  # Tamano horizontal de un A4
A4_height = 841.8897637795277 # Tamano vertical de un A4

# Cualidades de nuestro documento---------------
rightMargin = 72
leftMargin = 72
topMargin = 72
bottomMargin = 50

font = 'Helvetica'
font_bold = 'Helvetica-Bold'
font_size = 12
c.setFont(font, font_size)

salto_linea = 13
#-----------------------------------------------

# Disenamos la portada
c.setFont('Times-Roman', 60)
text_len = c.stringWidth(output_name, 'Times-Roman', 60)
c.drawString((A4_width/2)-(text_len/2), A4_height-350, output_name)
c.showPage()

# Rellenamos el documento con cada idioma y cada subfichero
for info in informacion:
    # Leemos los idiomas uno a uno
    idioma_leido = info[0]
    if debug == True: print('\t- Idioma leido: ', idioma_leido)
    leidos = 1

    # Escribimos una portada para cada idioma
    c.setFont('Times-Roman', 46)
    c.setFillColorRGB(199/255, 0/255, 57/255)
    text_len = c.stringWidth(idioma_leido, 'Times-Roman', 46)
    c.rect(leftMargin, A4_height-300, A4_width - leftMargin - rightMargin, -salto_linea*6, fill=1, stroke=0)
    from reportlab.lib.colors import white, red, black
    c.setFillColor(white)
    c.drawString((A4_width/2)-(text_len/2), A4_height-350, idioma_leido)
    c.showPage()

    # Funcion a usar para escribir las lienas
    from writeLine import writeLine

    # Leemos los ficheros pertenecientes a un idioma, uno a uno
    while leidos < len(info):
        # Leemos contenidos
        nombre_fichero = info[leidos][:-4]
        contenido_fichero = info[leidos+1]
        if debug == True: print('\t\t+ Fichero: ',nombre_fichero)

        # Escribimos en pdf
        # Una nueva pagina al comienzo de cada fichero
        longitud_restante_copia = A4_height-topMargin
        longitud_restante = longitud_restante_copia
        # Escribimos el nombre del fichero
        c.setFillColorRGB(199/255, 142/255, 0/255)
        c.rect(leftMargin, longitud_restante - salto_linea - 2, A4_width- leftMargin - rightMargin, salto_linea+10, fill=1, stroke=0)
        c.setFillColor(white)
		# Escribimos el texto dentro
        c.setFont(font_bold, font_size)
        c.drawString(leftMargin + 5, longitud_restante - salto_linea*0.5, nombre_fichero)
        c.setFont(font, font_size)
        c.setFillColor(black)
        # Restamos dos lineas de uso
        longitud_restante = longitud_restante - salto_linea*4

        for linea in contenido_fichero:
            # Escribimos la linea usando la funcion auxiliar
        	longitud_restante = writeLine(c, linea, rightMargin, leftMargin, topMargin, bottomMargin, font, font_bold, font_size, salto_linea, longitud_restante, A4_width, A4_height)
        	if debug == False: print('\t\t+ Longitud restante: ',longitud_restante)
        	# Comprobamos que aun la pagina tenga sitio
        	if(longitud_restante <= bottomMargin): # Si ya hemos completado una pagina
        		longitud_restante = A4_height - salto_linea # Reseteamos el contador para una nueva linea
        		c.showPage() # Pasamos la pagina


        # Pasamos de pagina al terminar la actual
        c.showPage()

        # Actualizamos variable de control
        leidos += 2

'''

    X.- Finaliza el programa

'''
print('\nX.- Finaliza el programa\n')

# Guardamos el documento
c.save()

# Abrimos el archivo pfdcon "evince"
import os
os.system('evince '+output_name+'.pdf')
