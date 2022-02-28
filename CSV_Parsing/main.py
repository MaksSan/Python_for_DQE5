import os
import sys
import csv
from classes import News
from classes import Advertisement
from classes import Vacancy

file_name = "Processed_file/file.txt"


def show_menu():                                                                                                        #function for printing menu
    print("Menu" + "\n" + "1 - Add news" + "\n" + "2 - Add advertisement" + "\n" + "3 - Add vacancy" + "\n" +
          "4 - Add text from input file" + "\n" + "5 - Exit" + "\n" + "\n")


def create_message_input():                                                                                             #function for input the text
    return input("Enter the text: ")


def parse_str(s, base=10, val=None):                                                                                    #function for str parsing
    try:
        return int(s, base)
    except ValueError:
        return val


def digital_input_format():                                                                                             #checking the input format
    x = input()
    while type(parse_str(x)) != int or int(x) <= 0:
        print('Incorrect input format or type, try again!')
        x = input("Try again: ")
    return x


def letter_input_format():                                                                                              #checking the input format
    x = input()
    while not x.isalpha():
        print('Incorrect input format or type, only letter can be used!')
        x = input("Try again: ")
    return x


def get_text_from_file(input_file):                                                                                     #function for get input file
    try:
        with open(input_file, 'r') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print('The file not exist!')
        sys.exit()


def normalize(text):                                                                                                    #function for normalization of file
    normalized_text = text.lower().replace('\t', '')
    general_text = list()
    add_ent = list()
    for x in normalized_text.split('\n'):
        for j in x.split('. '):
            if len(j) > 0:
                general_text.append(j.strip().capitalize())
    first_text = '\n'.join(general_text)
    for k in first_text.split('\n'):
        if k in ('News', 'Advertisement', 'Vacancy'):
            k = '\n' + k
        add_ent.append(k)
    new_text = '. \n'.join(add_ent)
    return new_text


def writing_to_file(file_name, text):                                                                                   #function for writing into the file
    with open(file_name, "a+") as file:
        file.write(text)
    return file


def get_directory():                                                                                                    #enter directory
    global directory
    print("File Selection menu" + "\n" + "1 - Enter path to file manually" + "\n"
          + '2 - File uploaded into "Input_file" folder' + "\n")
    while "2":
        cmd = input('Enter the menu item: ')
        if cmd == '1':
            directory = input('Enter the directory for file: ')
            while not os.path.exists(directory):
                print('File not found!')
                directory = input('Please try again: ')
            break
        elif cmd == '2':
            directory = "Input_file/input_text.txt"
            break
        else:                                                                                                           #if the nothing entered
            print("There is no such command!" + "\n")
    return directory


def words_counter():
    for char in '-.,\n':                                                                                                #cleaning text and lower casing all words
        text = get_text_from_file(file_name).replace(char, ' ').lower()
    word_list = text.split()                                                                                            #split returns a list of words delimited by sequences of whitespace (including tabs, newlines, etc, like re's \s)
    d = {}
    for word in word_list:
        if word.isalpha():
            d[word] = d.get(word, 0) + 1
    return d


def writing_to_csv1():                                                                                                  #writing to csv file
    finish_list = []
    with open('word_counter.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for key, value in words_counter().items():
            finish_list.append(key + ' - ' + str(value))
        for i in finish_list:
            writer.writerow([i])


def count_letters(text):                                                                                                #calculate the total of letters
    count = 0
    for i in text:
        if i.isalpha():
            count += 1
    return count


def get_unique_letters():                                                                                               #finding unique letters
    list_of_unique_letters = []
    for i in get_text_from_file(file_name):
        if i.isalpha():
            list_of_unique_letters.append(i)
    unique_letters = set(list_of_unique_letters)
    return unique_letters


def get_letter_count(letter, text):                                                                                     #getting count for all letters
    return text.count(letter)


def get_count_uppercase(letter, text):                                                                                  #getting count for uppercase letters
    count = 0
    for i in text:
        if i == letter and i.istitle():
            count += 1
    return count


def get_letter_percentage(letter, text):                                                                                #calculating percentage
    total = count_letters(text)
    return (get_letter_count(letter, text)/total) * 100


def writing_to_csv2():                                                                                                  #writing second csv file
    text = get_text_from_file(file_name)
    with open('letters_counter.csv', 'w', newline='') as csvfile:
        headers = ['letter', 'count_all', 'count_uppercase', 'percentage']
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        for i in get_unique_letters():
            writer.writerow({'letter': i, 'count_all': str(get_letter_count(i, text)), 'count_uppercase':
                str(get_count_uppercase(i, text)), 'percentage': str(round(get_letter_percentage(i, text), 2)) + '%'})


def input_text():                                                                                                       #main function for adding data
    while "N":
        cmd = input("Do you want to add an event? (Y/N) ").upper()
        if cmd == "Y":
            while "5":                                                                                                  #cycle for selecting menu
                cmd = input("Enter the number of the menu item: ")
                if cmd == "1":                                                                                          #condition for adding news
                    print("1 was selected" + "\n")
                    print("Enter the city: ")                                                                           #input city
                    city = letter_input_format()
                    mess = News(create_message_input(), city)
                    mess.write_to_file(file_name)                                                                       #using function for writing from class
                    writing_to_csv1()
                    writing_to_csv2()
                elif cmd == "2":                                                                                        #condition for addin Advertisements
                    print("2 was selected" + "\n")
                    print("Enter days count: ")                                                                         #input days count
                    days_count = digital_input_format()
                    mess = Advertisement(create_message_input(), days_count)
                    mess.write_to_file(file_name)                                                                       #using function for writing from class
                    writing_to_csv1()
                    writing_to_csv2()
                elif cmd == "3":                                                                                        #condition for addin vacancy
                    print("3 was selected" + "\n")
                    print("Enter the city: ")                                                                           #input city
                    city = letter_input_format()
                    print("Enter the position: ")
                    position = input()
                    print('Enter salary: ')
                    salary = digital_input_format()
                    mess = Vacancy(create_message_input(), salary, city, position)
                    mess.write_to_file(file_name)                                                                       #using function for writing from class
                    writing_to_csv1()
                    writing_to_csv2()
                elif cmd == "4":
                    print("4 was selected" + "\n")
                    directory = get_directory()
                    writing_to_file(file_name, normalize(get_text_from_file(directory)))
                    print("The data from the file was successfully recorded")
                    path = os.path.join(os.path.abspath(os.path.dirname(directory)), 'input_text.txt')                  #finding location for file
                    os.remove(path)                                                                                     #remove the file from folder
                    writing_to_csv1()
                    writing_to_csv2()
                    if os.path.isfile(directory):                                                                       #checking for the existence of a file
                        print("File not deleted")
                    else:
                        print('File was delete successfully')
                elif cmd == "5":
                    print('You have exited the add event menu!')
                    break
                else:                                                                                                   #if the nothing entered
                    print("There is no such command!" + "\n")
                    break
        elif cmd == "N":
            print('You have exited the program!')
            break
        else:
            print("There is no such command!" + "\n")
            break
    return


if __name__ == '__main__':                                                                                              #launching the "main"
    my_file = open(file_name)
    my_file.close()
    show_menu()
    input_text()
