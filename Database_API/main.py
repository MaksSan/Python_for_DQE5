import os
import sys
import csv
import json
import xml.etree.ElementTree as ET
import pyodbc
from classes import News
from classes import Advertisement
from classes import Vacancy
from classes import DBManager

file_name = "Processed_file/file.txt"
connection_string = ('info.db')
# connection_string = ('DRIVER={SQLite3 ODBC Driver};Direct=True;DATABASE=info.db;String Types = Unicode')


def show_menu():                                                                                                        #function for printing menu
    print("Menu" + "\n"
          + "1 - Add news" + "\n"
          + "2 - Add advertisement" + "\n"
          + "3 - Add vacancy" + "\n"
          + "4 - Add text from input file" + "\n"
          + "5 - Add text from JSON input file" + "\n"
          + "6 - Add text from XML input file" + "\n"
          + "7 - Exit" + "\n" + "\n")


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
    print("File Selection menu" + "\n"
          + "1 - Enter path to file manually" + "\n"
          + '2 - TXT File uploaded into "Input_file" folder' + "\n"
          + '3 - JSON File uploaded into "Input_file" folder' + "\n"
          + '4 - XML File uploaded into "Input_file" folder' + "\n")
    while "4":
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
        elif cmd == '3':
            directory = "Input_file/input_text.json"
            break
        elif cmd == '4':
            directory = "Input_file/input_text.xml"
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


def get_text_from_json_file(input_file):                                                                                #function for getting text from json file
    try:
        with open(input_file) as json_file:
            data = json.load(json_file)
        return data
    except FileNotFoundError:
        print('The file not exist!')
        sys.exit()


def get_news(data):                                                                                                     #function for finding 'News" element
    text = []
    for i in data['News']:
        text = ''.join(i["type"] + '\n' + i["text"] + '\n' + i["city"] + ', ' + i["date"] + '\n\n\n')
    return text


def get_vacancy(data):                                                                                                  #function for finding 'Vacancy" element
    text = []
    for i in data['Vacancy']:
        text = ''.join(i["type"] + '\n' + "Position: " + i["position"] + '\n' + "Experience: " + i["experience"] + '\n'
                       + "Salary: " + i["salary"] + '\n' + i["city"] + ', ' + i["date"] + '\n\n\n')
    return text


def get_advertisement(data):                                                                                            #function for finding 'Advertisment" element
    text = []
    for i in data['Advertisement']:
        text = ''.join(i["type"] + '\n' + i["text"] + '\n' + "Actual until: " + i["actual_until"] + '\n\n\n')
    return text


def get_xml_file(input_file):                                                                                           #function for getting structure xml file
    try:
        root = ET.parse(input_file)
        return root
    except FileNotFoundError:
        print('The file not exist!')
        sys.exit()


def get_text_from_xml(root):                                                                                            #function for getting text from xml
    text = []
    for i in root.iter():
        text.append(i.text)
    new_text = '\n'.join(text)
    return new_text


def input_text():                                                                                                       #main function for adding data
    while "N":
        cmd = input("Do you want to add an event? (Y/N) ").upper()
        if cmd == "Y":
            while "6":                                                                                                  #cycle for selecting menu
                cmd = input("Enter the number of the menu item: ")
                if cmd == "1":                                                                                          #condition for adding news
                    print("1 was selected" + "\n")
                    print("Choose the recording method" + "\n"
                          + "1 - Recording into the TXT file" + "\n"
                          + '2 - Recording into the Data Base' + "\n")
                    cmd = input('Enter the menu item: ')
                    if cmd == '1':
                        print("Enter the city: ")                                                                       #input city
                        city = letter_input_format()
                        mess = News(create_message_input(), city)
                        mess.write_to_file(file_name)                                                                   #using function for writing from class
                        writing_to_csv1()
                        writing_to_csv2()
                    else:
                        print("Enter the city: ")                                                                       # input city
                        city = letter_input_format()
                        mess = News(create_message_input(), city)
                        dbmanager = DBManager(connection_string)
                        dbmanager.write_to_news(mess.gettext(), mess.get_city(), mess.get_datetime())                   #adding into News data base
                elif cmd == "2":                                                                                        #condition for addin Advertisements
                    print("2 was selected" + "\n")
                    print("Choose the recording method" + "\n"
                          + "1 - Recording into the TXT file" + "\n"
                          + '2 - Recording into the Data Base' + "\n")
                    cmd = input('Enter the menu item: ')
                    if cmd == '1':
                        print("Enter days count: ")                                                                     #input days count
                        days_count = digital_input_format()
                        mess = Advertisement(create_message_input(), days_count)
                        mess.write_to_file(file_name)                                                                   #using function for writing from class
                        writing_to_csv1()
                        writing_to_csv2()
                    else:
                        print("Enter days count: ")
                        days_count = digital_input_format()
                        mess = Advertisement(create_message_input(), days_count)
                        dbmanager = DBManager(connection_string)
                        dbmanager.write_to_advertisement(mess.gettext(), str(mess.get_date() + " "
                                                                             + mess.get_days_count() + " days left"))   #adding into Advertisement data base
                elif cmd == "3":                                                                                        #condition for adding vacancy
                    print("3 was selected" + "\n")
                    print("Choose the recording method" + "\n"
                          + "1 - Recording into the TXT file" + "\n"
                          + '2 - Recording into the Data Base' + "\n")
                    cmd = input('Enter the menu item: ')
                    if cmd == '1':
                        print("Enter the city: ")                                                                       #input city
                        city = letter_input_format()
                        print("Enter the position: ")
                        position = input()
                        print('Enter salary: ')
                        salary = digital_input_format()
                        mess = Vacancy(create_message_input(), salary, city, position)
                        mess.write_to_file(file_name)                                                                   #using function for writing from class
                        writing_to_csv1()
                        writing_to_csv2()
                    else:
                        print("Enter the city: ")                                                                       # input city
                        city = letter_input_format()
                        print("Enter the position: ")
                        position = input()
                        print('Enter salary: ')
                        salary = digital_input_format()
                        mess = Vacancy(create_message_input(), salary, city, position)
                        dbmanager = DBManager(connection_string)
                        dbmanager.write_to_vacancy(mess.get_position(), mess.gettext(), str(mess.get_salary() + "$"),
                                                   mess.get_city(), mess.get_datetime())                                #adding into Vacancy data base

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
                    print("5 was selected" + "\n")
                    directory = get_directory()
                    writing_to_file(file_name, get_news(get_text_from_json_file(directory))
                                    + get_vacancy(get_text_from_json_file(directory))
                                    + get_advertisement(get_text_from_json_file(directory)))
                    print("The data from the file was successfully recorded")
                    path = os.path.join(os.path.abspath(os.path.dirname(directory)), 'input_text.json')
                    os.remove(path)
                    writing_to_csv1()
                    writing_to_csv2()
                    if os.path.isfile(directory):                                                                       # checking for the existence of a file
                        print("File not deleted")
                    else:
                        print('File was delete successfully')
                elif cmd == "6":
                    print("6 was selected" + "\n")
                    directory = get_directory()
                    writing_to_file(file_name, get_text_from_xml(get_xml_file(directory)))
                    print("The data from the file was successfully recorded")
                    path = os.path.join(os.path.abspath(os.path.dirname(directory)), 'input_text.xml')
                    os.remove(path)
                    writing_to_csv1()
                    writing_to_csv2()
                    if os.path.isfile(directory):                                                                       # checking for the existence of a file
                        print("File not deleted")
                    else:
                        print('File was delete successfully')
                elif cmd == "7":
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

