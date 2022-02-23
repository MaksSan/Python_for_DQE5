from classes import News
from classes import Advertisement
from classes import Vacancy

file_name = "Processed_file/file.txt"
input_file = "Input_file/input_text.txt"


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
    with open(input_file, 'r') as file:
        text = file.read()
    return text


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
                elif cmd == "2":                                                                                        #condition for addin Advertisements
                    print("2 was selected" + "\n")
                    print("Enter days count: ")                                                                         #input days count
                    days_count = digital_input_format()
                    mess = Advertisement(create_message_input(), days_count)
                    mess.write_to_file(file_name)                                                                       #using function for writing from class
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
                elif cmd == "4":
                    print("4 was selected" + "\n")
                    try:
                        writing_to_file(file_name, normalize(get_text_from_file(input_file)))
                    except IndexError:
                        print(f'Index is out of range')
                    print("The data from the file was successfully recorded")
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


if __name__ == '__main__':
    my_file = open(file_name)
    my_file.close()
    show_menu()
    input_text()                                                                                                        #launching the function "main"
