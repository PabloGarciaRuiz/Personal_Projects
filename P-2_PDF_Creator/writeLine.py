'''

    Funcion Principal

'''
def writeLine(c, linea, rightMargin, leftMargin, topMargin, bottomMargin, font, font_bold, font_size, salto_linea, longitud_restante, A4_width, A4_height):
    # Mientras una pagina tenga espacio aun la rellenamos

    # Eliminamos el ultimo caracter, si la linea contiene un '\n'
    if '\n' in linea:
    	linea = linea[:-1]

    # Comprobamos los distintos casos de linea a escribir
    if ':' in linea:  # Nos encontramos con una definicion
    	pos = 0
    	for caracter in linea:
    		if caracter == ':':
    			break
    		pos += 1

    	linea_first = linea[:pos+1]
    	linea_second = linea[pos+1:]

    	c.setFont(font_bold, font_size)
    	c.drawString(leftMargin, longitud_restante, linea_first)
    	text_len = c.stringWidth(linea_first, font_bold, font_size)
    	c.setFont(font, font_size)
    	c.drawString(leftMargin+text_len, longitud_restante, linea_second)
    	# Restamos una linea de uso
    	longitud_restante = longitud_restante - salto_linea


    elif '---' in linea[:3]: # LINEA SEPARADORA SIN ESPACIOS EXTRA
    	# Escribimos la linea separadora
    	c.line(leftMargin, longitud_restante, A4_width-rightMargin, longitud_restante)
    	# Restamos una lineas de uso
    	longitud_restante = longitud_restante - salto_linea

    elif '-----' in linea[:4]: # LINEA SEPARADORA CON UN ESPACIO EXTRA
    	# Escribimos la linea separadora
    	c.line(leftMargin, longitud_restante, A4_width-rightMargin, longitud_restante)
    	# Restamos 2 lineas de uso (para anadir 1 separacion extra debajo)
    	longitud_restante = longitud_restante - salto_linea*2

    elif '-----' in linea[:5]: # LINEA SEPARADORA CON DOS ESPACIOS EXTRA
    	# Escribimos la linea separadora
    	c.line(leftMargin, longitud_restante, A4_width-rightMargin, longitud_restante)
    	# Restamos 3 lineas de uso (para anadir 2 separaciones extra debajo)
    	longitud_restante = longitud_restante - salto_linea*3

    elif '------' in linea[:6]: # LINEA SEPARADORA CON TRES ESPACIOS EXTRA
    	# Escribimos la linea separadora
    	c.line(leftMargin, longitud_restante, A4_width-rightMargin, longitud_restante)
    	# Restamos 4 lineas de uso (para anadir 3 separaciones extra debajo)
    	longitud_restante = longitud_restante - salto_linea*4


    elif '[]<-' in linea[:4]: # CAJITA CON TEXTO
    	# Extraemos el texto que se quiere colocar en la cajita
    	texto = linea[4:]
    	c.rect(leftMargin, longitud_restante- salto_linea - 2, A4_width- leftMargin - rightMargin, salto_linea+10, fill=0)
    	# Escribimos el texto dentro
    	c.setFont(font_bold, font_size)
    	c.drawString(leftMargin + 5, longitud_restante - salto_linea*0.5, texto)
    	c.setFont(font, font_size)
    	# Restamos dos lineas de uso
    	longitud_restante = longitud_restante - salto_linea*2

    elif '[]' in linea[:2]: # CAJITA EN BLANCO PARA RELLENARLA
    	# Dibujamos un rectangulo
    	c.rect(leftMargin, longitud_restante- salto_linea - 2, A4_width- leftMargin - rightMargin, salto_linea+10, fill=0)
    	# Restamos dos lineas de uso
    	longitud_restante = longitud_restante - salto_linea*2


    else: # LINEA NORMAL
    	# Escribimos la linea si no tiene nada de especial
    	c.drawString(leftMargin, longitud_restante, linea)
    	# Restamos una linea de uso
    	longitud_restante = longitud_restante - salto_linea

    return longitud_restante
