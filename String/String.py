original_text = '''homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph. 

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.'''

num_whitespace = 0
general_text = list()
collected_sentence = list()

for c in original_text:                                                                                                 #counting the number of all whitespaces
    if c in {' ', '\n', '\t'}:
        num_whitespace += 1

replaced_text = original_text.lower().replace(' iz ', ' is ').replace('\t', '').replace('\n', '')                       #replacements

try:                                                                                                                    #checking for error
    for x in replaced_text.split('. '):                                                                                 #splitting all text by dot
        if len(x) > 0:                                                                                                  #condition for not zero leng
            general_text.append(x.strip().capitalize())                                                                 #adding sentences/removing spaces at the begin/capital letler for fIrst words
            collected_sentence.append(x.split()[-1])                                                                    #creating sentence with last words of each existing sentence
except IndexError:                                                                                                      #expected exception
    print(f'Index is out of range')                                                                                     #printing text error

new_text = '. \n'.join(general_text) + '\n' + ' '.join(collected_sentence).capitalize()                                 #joining general text with sentence from last words

print(f'Normalized text: \n{new_text}')
print(f'\n=================================')
print(f'Numbers of whitespaces: {num_whitespace}')
print(f'=================================')
