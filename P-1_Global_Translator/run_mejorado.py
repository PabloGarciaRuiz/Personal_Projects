# Debug mode
debug = False


'''#............................

	1.- READING INPUT FOLDER

'''#............................

# We read the input folder, and transform it into a matrix
# where each element is a cumulous of lines of each file

import os

# We prove that the Inputs folder exists
if os.path.isdir('Inputs'):
	# La carpeta existe
	if debug == True:
		print("Se ha leido la carpeta 'Inputs' correctamente")
else:
	# La carpe no existe, error
	print("ERROR: Inputs folder doesn't exists")
	exit()

# We list and read the files
from os import listdir
count = 0
for file in listdir('Inputs'):
	f = open('Inputs/'+file, 'r')
	content = f.readlines()
	#Insertamos nombres y contenidos de cada fichero
	if count == 0:
		ficheros_nombres = file
		ficheros_contenidos = content
	elif count == 1:
		ficheros_nombres = [ficheros_nombres, file]
		ficheros_contenidos = [ficheros_contenidos, content]
	else:
		ficheros_nombres.append(file)
		ficheros_contenidos.append(content)
	count += 1

# Numero de ficheros
if debug == True:
	print('Numero de ficheros en Inputs folder: ', len(ficheros_nombres))
	print('Numero de ficheros en Inputs folder: ', len(ficheros_contenidos))
	for i in ficheros_nombres:
		print(i)


# Printing the content of the files
count = 0
for i in ficheros_contenidos:
	if debug == True:
		print('--- Fichero: ',ficheros_nombres[count],' ---')
	count2 = 0
	for x in i:
		x = x.replace('\n','') # Eliminamos saltos de linea de cada line
		ficheros_contenidos[count][count2] = x # Guardamos cambios
		if debug == True:
			print('"',x,'"')
		count2 += 1
	count += 1

'''#...............................................................

	2.- PREPARING THE LANGUAGES WE WANT TO TRANSLATE THE INPUT TO

'''#...............................................................

# Language indexes
languages_indexes = ['af', 'sq', 'am', 'ar', 'hy', 'az', 'eu', 'be', 'bn', 'bs', 'bg', 'ca', 'ceb', 'ny', 'zh-cn', 'zh-tw', 'co', 'hr', 'cs', 'da', 'nl', 'en', 'eo', 'et', 'tl', 'fi', 'fr', 'fy', 'gl', 'ka', 'de', 'el', 'gu', 'ht', 'ha', 'haw', 'iw', 'hi', 'hmn', 'hu', 'is', 'ig', 'id', 'ga', 'it', 'ja', 'jw', 'kn', 'kk', 'km', 'ko', 'ku', 'ky', 'lo', 'la', 'lv', 'lt', 'lb', 'mk', 'mg', 'ms', 'ml', 'mt', 'mi', 'mr', 'mn', 'my', 'ne', 'no', 'ps', 'fa', 'pl', 'pt', 'pa', 'ro', 'ru', 'sm', 'gd', 'sr', 'st', 'sn', 'sd', 'si', 'sk', 'sl', 'so', 'es', 'su', 'sw', 'sv', 'tg', 'ta', 'te', 'th', 'tr', 'uk', 'ur', 'uz', 'vi', 'cy', 'xh', 'yi', 'yo', 'zu', 'he'] #Falta 'fil', da error
if debug == True:
	print('Numero de idiomas: ', len(languages_indexes))

# Languages names
languages_names = ['afrikaans', 'albanian', 'amharic', 'arabic', 'armenian', 'azerbaijani', 'basque', 'belarusian', 'bengali', 'bosnian', 'bulgarian', 'catalan', 'cebuano', 'chichewa', 'chinese (simplified)', 'chinese (traditional)', 'corsican', 'croatian', 'czech', 'danish', 'dutch', 'english', 'esperanto', 'estonian', 'filipino', 'finnish', 'french', 'frisian', 'galician', 'georgian', 'german', 'greek', 'gujarati', 'haitian creole', 'hausa', 'hawaiian', 'hebrew', 'hindi', 'hmong', 'hungarian', 'icelandic', 'igbo', 'indonesian', 'irish', 'italian', 'japanese', 'javanese', 'kannada', 'kazakh', 'khmer', 'korean', 'kurdish (kurmanji)', 'kyrgyz', 'lao', 'latin', 'latvian', 'lithuanian', 'luxembourgish', 'macedonian', 'malagasy', 'malay', 'malayalam', 'maltese', 'maori', 'marathi', 'mongolian', 'myanmar (burmese)', 'nepali', 'norwegian', 'pashto', 'persian', 'polish', 'portuguese', 'punjabi', 'romanian', 'russian', 'samoan', 'scots gaelic', 'serbian', 'sesotho', 'shona', 'sindhi', 'sinhala', 'slovak', 'slovenian', 'somali', 'spanish', 'sundanese', 'swahili', 'swedish', 'tajik', 'tamil', 'telugu', 'thai', 'turkish', 'ukrainian', 'urdu', 'uzbek', 'vietnamese', 'welsh', 'xhosa', 'yiddish', 'yoruba', 'zulu', 'Hebrew'] #Falta 'Filipino'
if debug == True:
	print('Numero de idiomas: ', len(languages_names))

# Print the languages
if debug == True:
	count = 0
	for value in languages_indexes:
		print('Language nº',count+1, ': ', value, ' -> ',languages_names[count])
		count += 1



'''#..................

	3.- TRANSLATING

'''#..................

from googletrans import Translator
from shutil import rmtree
# Initialise the translator
translator = Translator()
# Creates the principal outputs folder
if os.path.isdir('Outputs'):
	rmtree('Outputs')
	os.mkdir('Outputs')
else:
	os.mkdir('Outputs')

# Auxiliar Loop: in order to create a list of the languages in spanish
faux = open('Languages.txt', 'w')
count = 0
for lang in languages_names:
	result = translator.translate(lang, src='en', dest='es')
	faux.write('Nº' + str(count+1) + ' ' + lang + ': ' + result.text + '\n')
	count += 1
faux.close()

# Main Loop
count = 0
for lang in languages_indexes:
	# REINITIALIZE THE API  <-- Sometimes goes wrong the translations
	translator = Translator()
	# Printing information about the iterations
	print('Translating into language nº',count+1, ': ', lang, ' -> ',languages_names[count])

	# Creamos la carpeta del idioma
	os.mkdir('Outputs/'+str(count+1)+'_'+languages_names[count])

	# Leemos cada fichero y vamos traduciendolos uno a uno y por separado
	j = 0
	for file_name in ficheros_nombres:
		file_name_sin_extension = file_name.replace('.txt','')
		nombre_traducido = translator.translate(file_name_sin_extension, src='es', dest=lang)
		nuevo_nombre = file_name_sin_extension + '_' + nombre_traducido.text + '.txt'
		f = open('Outputs/'+str(count+1)+'_'+languages_names[count]+'/'+nuevo_nombre, 'w')

		# Borramos todos los '\n'
		k = 0
		for kk in ficheros_contenidos[j]:
			ficheros_contenidos[j][k] = ficheros_contenidos[j][k].replace('\n','')
			k += 1


		result = translator.translate(ficheros_contenidos[j], src='es', dest=lang)
		for r in result:
			# Si el primer caracter es un "#", no ponemos traduccion
			# (Se trata de un comentario)
			if r.origin[0] == '#':
				cadena_nueva = r.origin[1:]
				f.write(cadena_nueva+'\n')
			else:
				f.write(r.origin+' : '+r.text+'\n')
		f.close()
		j += 1

	count = count + 1


# END OF THE PROGRAM
print('\nSe ha traducido todo con exito!')
