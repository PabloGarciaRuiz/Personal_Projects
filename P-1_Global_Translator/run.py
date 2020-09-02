# Debug mode
debug = False


'''#....................

	READING INPUT FILE

'''#....................

# We read the input.txt file, and transform it into a vector
# where each element is a line of the previuos file
f = open('input.txt', 'r')
content = f.readlines()

#Print the contents of the file
if debug == True:
	count = 0
	for line in content:
		print("Line {}: {}".format(count, line.strip()))
		count += 1



'''#.............................................................

	PREPARING THE LANGUAGES WE WANT TO TRANSLATE THE INPUT TO

'''#.............................................................

# Language indexes
languages_indexes = ['af', 'sq', 'am', 'ar', 'hy', 'az', 'eu', 'be', 'bn', 'bs', 'bg', 'ca', 'ceb', 'ny', 'zh-cn', 'zh-tw', 'co', 'hr', 'cs', 'da', 'nl', 'en', 'eo', 'et', 'tl', 'fi', 'fr', 'fy', 'gl', 'ka', 'de', 'el', 'gu', 'ht', 'ha', 'haw', 'iw', 'hi', 'hmn', 'hu', 'is', 'ig', 'id', 'ga', 'it', 'ja', 'jw', 'kn', 'kk', 'km', 'ko', 'ku', 'ky', 'lo', 'la', 'lv', 'lt', 'lb', 'mk', 'mg', 'ms', 'ml', 'mt', 'mi', 'mr', 'mn', 'my', 'ne', 'no', 'ps', 'fa', 'pl', 'pt', 'pa', 'ro', 'ru', 'sm', 'gd', 'sr', 'st', 'sn', 'sd', 'si', 'sk', 'sl', 'so', 'es', 'su', 'sw', 'sv', 'tg', 'ta', 'te', 'th', 'tr', 'uk', 'ur', 'uz', 'vi', 'cy', 'xh', 'yi', 'yo', 'zu', 'he'] #Falta 'fil', da error
print('Numero de idiomas: ', len(languages_indexes))

# Languages names
languages_names = ['afrikaans', 'albanian', 'amharic', 'arabic', 'armenian', 'azerbaijani', 'basque', 'belarusian', 'bengali', 'bosnian', 'bulgarian', 'catalan', 'cebuano', 'chichewa', 'chinese (simplified)', 'chinese (traditional)', 'corsican', 'croatian', 'czech', 'danish', 'dutch', 'english', 'esperanto', 'estonian', 'filipino', 'finnish', 'french', 'frisian', 'galician', 'georgian', 'german', 'greek', 'gujarati', 'haitian creole', 'hausa', 'hawaiian', 'hebrew', 'hindi', 'hmong', 'hungarian', 'icelandic', 'igbo', 'indonesian', 'irish', 'italian', 'japanese', 'javanese', 'kannada', 'kazakh', 'khmer', 'korean', 'kurdish (kurmanji)', 'kyrgyz', 'lao', 'latin', 'latvian', 'lithuanian', 'luxembourgish', 'macedonian', 'malagasy', 'malay', 'malayalam', 'maltese', 'maori', 'marathi', 'mongolian', 'myanmar (burmese)', 'nepali', 'norwegian', 'pashto', 'persian', 'polish', 'portuguese', 'punjabi', 'romanian', 'russian', 'samoan', 'scots gaelic', 'serbian', 'sesotho', 'shona', 'sindhi', 'sinhala', 'slovak', 'slovenian', 'somali', 'spanish', 'sundanese', 'swahili', 'swedish', 'tajik', 'tamil', 'telugu', 'thai', 'turkish', 'ukrainian', 'urdu', 'uzbek', 'vietnamese', 'welsh', 'xhosa', 'yiddish', 'yoruba', 'zulu', 'Hebrew'] #Falta 'Filipino'
print('Numero de idiomas: ', len(languages_names))

# Print the languages
if debug == True:
	count = 0
	for value in languages_indexes:
		print('Language nº',count+1, ': ', value, ' -> ',languages_names[count])
		count += 1



'''#.............

	TRANSLATING

'''#.............

from googletrans import Translator
import os
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
	# Printing information about the iterations
	print('Translating into language nº',count+1, ': ', lang, ' -> ',languages_names[count])
	result = translator.translate(content, src='es', dest=lang)
	os.mkdir('Outputs/'+str(count+1)+'_'+languages_names[count])
	f = open('Outputs/'+str(count+1)+'_'+languages_names[count]+'/'+languages_names[count]+'.txt', 'w')
	
	for r in result:
		f.write(r.origin.replace('\n','')+' >>>>> '+r.text+'\n')
	f.close()
	count = count + 1
