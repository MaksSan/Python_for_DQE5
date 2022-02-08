def original_text():
    text = '''homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph. 

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.'''
    return text


def numbers_whitespaces():
    num_whitespaces = 0
    for c in original_text():
        if c in {' ', '\n', '\t'}:
            num_whitespaces += 1
    return num_whitespaces


def replace_text():
    replaced_text = original_text().lower().replace(' iz ', ' is ').replace('\t', '').replace('\n', '')
    return replaced_text


def general_text():
    gt = list()
    for x in replace_text().split('.'):
        if len(x) > 0:
            gt.append(x.strip().capitalize())
    return gt


def collect_general_text():
    coll_gen_text = '. \n'.join(general_text())
    return coll_gen_text


def sentence_last_words():
    slw = list()
    for x in general_text():
        if len(x) > 0:
            slw.append(x.split()[-1])
    slw = ' '.join(slw).capitalize()
    return slw


try:
    sentence_last_words()
except IndexError:
    print(f'Index is out of range')


def finish_text():
    nt = general_text()
    nt.insert(3, sentence_last_words())
    new_text = '. \n'.join(nt)
    return new_text


print(f'Normalized text: \n{finish_text()}.')
print(f'\n=================================')
print(f'Numbers of whitespaces: {numbers_whitespaces()}')
print(f'=================================')
