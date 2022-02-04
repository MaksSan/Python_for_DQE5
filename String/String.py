original_text = '''homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.'''

num_whitespace = 0
some_variable = []
strings = list()
strings1 = list()

for c in original_text:
    if c in {' ', '\n', '\t'}:
        num_whitespace += 1

replaced_text = original_text.lower().replace(' iz ', ' is ').replace('\t', '').replace('\t', '').replace('\n', '')

for x in replaced_text.split('.'):
    some_variable.append(x)
try:
    for x in replaced_text.split('. '):
        x = x.strip()
        x = x.capitalize()
        strings.append(x)
        c = x.split()
        strings1.append(c[-1])
except IndexError:
    print(f'Index is out of range')

newline = '. \n'.join(strings) + '\n' + ' '.join(strings1).capitalize()

print(f'=================================')
print(f'Numbers of whitespaces: {num_whitespace}')
print(f'=================================')
print(f'Normalized text: \n{newline}')
