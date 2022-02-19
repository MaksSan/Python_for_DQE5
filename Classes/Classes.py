import datetime

file_name = "file.txt"


class Message:                                                                                                          #class for using Inheritance

    def __init__(self, text):                                                                                           #function for initialization varibels
        self.text = text

    def gettext(self):                                                                                                  #function for getting inputed text
        return self.text


class News(Message):                                                                                                    #class for writing news

    def __init__(self, text, city):                                                                                     #function for initialization varibels
        super().__init__(text)
        self.city = city

    def get_city(self):                                                                                                 #function for getting the city
        return self.city

    def write_to_file(self, file_name):                                                                                 #function for writing text into the file
        with open(file_name, "a+") as _file:                                                                            #open at the end on the file
            _file.write("NEWS----------------------" + "\n" + self.text + "\n" + self.city + ", " +
                        str(datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')) + "\n\n\n\n")                        #write text and date into the file


class Advertisement(Message):                                                                                           #class for writing Advertisement

    def __init__(self, text, days_count):                                                                               #function for initialization varibels
        super().__init__(text)
        self.days_count = days_count

    def get_days_count(self):                                                                                           #function for getting count of days
        return self.days_count

    def get_date(self):                                                                                                 #function to calculate the remainder of day
        add_days = int(self.days_count)                                                                                 #varible for count of days
        date_format = '%d/%m/%Y'                                                                                        #initialization of format
        time_now = datetime.datetime.now()                                                                              #finding date for now
        if add_days != 0:
            another_time = time_now + datetime.timedelta(days=add_days)                                                 #calculate the remainder of day
        else:
            another_time = time_now

        return another_time.strftime(date_format)

    def write_to_file(self, file_name):                                                                                 #function for writing text into the file
        with open(file_name, "a+") as _file:                                                                            #open at the end on the file
            _file.write("Advertisement------------------------" + "\n" + self.text + "\n" + "Actual until: " +
                        self.get_date() + " " + self.get_days_count() + " days left" "\n\n\n\n")                        #write text and date into the file


class Vacancy(Message):                                                                                                 #class for writing Advertisement

    def __init__(self, text, city):                                                                                     #function for initialization varibels
        super().__init__(text)
        self.city = city

    def get_city(self):                                                                                                 #function for getting the city
        return self.city

    def write_to_file(self, file_name):                                                                                 #function for writing text into the file
        with open(file_name, "a+") as _file:                                                                            #open at the end on the file
            _file.write("Vacancy--------------------" + "\n" + self.text + "\n" + self.city + ", " +
                        str(datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')) + "\n\n\n\n")                        #write text and date into the file


def show_menu():                                                                                                        #function for printing menu
    print("Menu" + "\n" + "1 - Add news" + "\n" + "2 - Add advertisement" + "\n" + "3 - Add vacancy" + "\n" +
          "4 - Exit" + "\n" + "\n")


def create_message_input():                                                                                             #function for input the text
    return input("Input text: ")


def input_text():                                                                                                       #Main function for adding data
    cmd = input("Input command: ")                                                                                      #input command
    while cmd != "4":                                                                                                   #cycle for selecting menu
        if cmd == "1":                                                                                                  #condition for adding news
            print("1 was selected" + "\n")
            city = input("Input the city: ")                                                                            #input city
            mess = News(create_message_input(), city)
            mess.write_to_file(file_name)                                                                               #using function for writing from class
            break
        elif cmd == "2":                                                                                                #condition for addin Advertisements
            print("2 was selected" + "\n")
            days_count = input("Input days count: ")                                                                    #input days count
            mess = Advertisement(create_message_input(), days_count)
            mess.write_to_file(file_name)                                                                               #using function for writing from class
            break
        elif cmd == "3":                                                                                                #condition for addin vacancy
            print("3 was selected" + "\n")
            city = input("Input the city: ")                                                                            #input city
            mess = Vacancy(create_message_input(), city)
            mess.write_to_file(file_name)                                                                               #using function for writing from class
            break
        else:                                                                                                           #if the nothing entered
            print("There is no such command!" + "\n")
            break
    return


def main():                                                                                                             #function for working with file and print the menu
    my_file = open(file_name)
    my_file.close()
    show_menu()
    input_text()


main()                                                                                                                  #launching the programm

