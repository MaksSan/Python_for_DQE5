import datetime
import abc

file_name = "file.txt"


class Message:

    def __init__(self, text):
        self.text = text

    def gettext(self):
        return self.text

    @abc.abstractmethod
    def write_to_file(self, _filename):
        with open(_filename, "a+") as _file:
            _file.write(self.text + "\n" + str(datetime.datetime.now()) + "\n\n\n\n")


class News(Message):

    def __init__(self, text, city):
        super().__init__(text)
        self.city = city

    def get_city(self):
        return self.city

    def write_to_file(self, _filename):
        with open(_filename, "a+") as _file:
            _file.write("NEWS----------------------" + "\n" + self.text + "\n" + self.city + ", " + str(datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')) + "\n\n\n\n")


class Advertisement(Message):

    def __init__(self, text, days_count):
        super().__init__(text)
        self.days_count = days_count

    def get_days_count(self):
        return self.days_count

    def get_date(self):
        add_days = int(self.days_count)
        date_format = '%d/%m/%Y'
        time_now = datetime.datetime.now()
        if add_days != 0:
            another_time = time_now + datetime.timedelta(days=add_days)
        else:
            another_time = time_now

        return another_time.strftime(date_format)

    def write_to_file(self, _filename):
        with open(_filename, "a+") as _file:
            _file.write("Advertisement------------------------" + "\n" + self.text + "\n" + "Actual until: " + self.get_date() + " " + self.get_days_count() + " days left" "\n\n\n\n")


class Vacancy(Message):

    def __init__(self, text, city):
        super().__init__(text)
        self.city = city

    def get_city(self):
        return self.city

    def write_to_file(self, _filename):
        with open(_filename, "a+") as _file:
            _file.write("Vacancy-----------------" + "\n" + self.text + "\n" + self.city + ", " + str(datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')) + "\n\n\n\n")


def show_menu():
    print("Menu" + "\n" + "1 - Add news" + "\n" + "2 - Add advertisement" + "\n" + "3 - Add vacancy" + "\n" + "4 - Exit" + "\n" + "\n")


def create_message_input():
    return input("Input text: ")


def main():
    my_file = open(file_name)
    my_file.close()
    show_menu()
    input_text()


def input_text():
    cmd = input("Input command: ")
    while cmd != "4":
        if cmd == "1":
            print("1 was selected" + "\n")
            _city = input("Input the city: ")
            _mess = News(create_message_input(), _city)
            _mess.write_to_file(file_name)
            break
        elif cmd == "2":
            print("2 was selected" + "\n")
            days_count = input("Input days count: ")
            _mess = Advertisement(create_message_input(), days_count)
            _mess.write_to_file(file_name)
            break
        elif cmd == "3":
            print("3 was selected" + "\n")
            _city = input("Input the city: ")
            _mess = Vacancy(create_message_input(), _city)
            _mess.write_to_file(file_name)
            break
        else:
            print("There is no such command!" + "\n")
            break
    return


main()

