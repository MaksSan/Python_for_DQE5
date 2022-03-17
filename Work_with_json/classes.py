import datetime


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
        with open(file_name, "a+") as file:                                                                             #open at the end on the file
            file.write("News" + "\n" + self.text + "\n" + self.get_city() + ", " +
                       str(datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')) + "\n")                               #write text and date into the file


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
        with open(file_name, "a+") as file:                                                                             #open at the end on the file
            file.write("Advertisement" + "\n" + self.text + "\n" + "Actual until: " +
                       self.get_date() + " " + self.get_days_count() + " days left" "\n")                               #write text and date into the file


class Vacancy(Message):                                                                                                 #class for writing Advertisement

    def __init__(self, text, salary, city, position):                                                                   #function for initialization varibels
        super().__init__(text)
        self.city = city
        self.salary = salary
        self.position = position

    def get_city(self):                                                                                                 #function for getting the city
        return self.city

    def get_salary(self):                                                                                               #function for getting the city
        return self.salary

    def write_to_file(self, file_name):                                                                                 #function for writing text into the file
        with open(file_name, "a+") as file:                                                                             #open at the end on the file
            file.write("Vacancy" + "\n" + "Position: " + self.position + "\n" + self.text + "\n" +
                       "Salary: " + self.get_salary() + "$" + "\n" + self.get_city() + ", " +
                       str(datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')) + "\n")                               #write text and date into the file


