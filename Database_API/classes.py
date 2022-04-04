import datetime
import pyodbc
import sqlite3


class Message:                                                                                                          #class for using Inheritance

    def __init__(self, text):                                                                                           #function for initialization varibels
        self.text = text

    def gettext(self):                                                                                                  #function for getting inputed text
        return self.text


class News(Message):                                                                                                    #class for writing news

    def __init__(self, text, city):                                                                                     #function for initialization varibels
        super().__init__(text)
        self.city = city
        self.date_time = datetime.datetime.now()

    def get_city(self):                                                                                                 #function for getting the city
        return self.city

    def get_datetime(self):
        return str(self.date_time.strftime('%d/%m/%Y %H:%M:%S'))

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
        self.date_time = datetime.datetime.now()

    def get_city(self):                                                                                                 #function for getting the city
        return self.city

    def get_salary(self):                                                                                               #function for getting the city
        return self.salary

    def get_datetime(self):
        return str(self.date_time.strftime('%d/%m/%Y %H:%M:%S'))

    def get_position(self):
        return self.position

    def write_to_file(self, file_name):                                                                                 #function for writing text into the file
        with open(file_name, "a+") as file:                                                                             #open at the end on the file
            file.write("Vacancy" + "\n" + "Position: " + self.position + "\n" + self.text + "\n" +
                       "Salary: " + self.get_salary() + "$" + "\n" + self.get_city() + ", " +
                       self.get_datetime() + "\n")                                                                      #write text and date into the file


class DBManager:
    def __init__(self, connection_string):
        self.cur = None
        self.connection_string = connection_string

    def write_to_news(self, text, city, date):                                                                          #function for writing into News data base
        with sqlite3.connect(self.connection_string) as self.conn:
            self.cur = self.conn.cursor()
            print("Connection to SQLite DB successful")
        news_table = self.cur.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='news' ''') #verification existing table in DB
        if news_table.fetchone()[0] == 1:
            pass
        else:
            self.cur.execute('CREATE TABLE news (type varchar(50), text varchar(250), '
                             'city varchar(100), date varchar(100))')                                                   #creating News table
            print('Table was successfully created.')
        self.cur.execute(f"INSERT INTO news (type, text, city, date) VALUES ('News', '{text}', '{city}', '{date}')")    #insert data into the table
        self.conn.commit()

    def write_to_advertisement(self, text, actual_until):                                                               #function for writing into advertisement data base
        with sqlite3.connect(self.connection_string) as self.conn:
            self.cur = self.conn.cursor()
            print("Connection to SQLite DB successful")
        news_table = self.cur.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' 
        AND name='advertisement' ''')                                                                                   #verification existing table in DB
        if news_table.fetchone()[0] == 1:
            pass
        else:
            self.cur.execute('CREATE TABLE advertisement (type varchar(50), text varchar(250), '
                             'actual_until varchar(100))')                                                              #creating advertisement table
            print('Table was successfully created.')
        self.cur.execute(f"INSERT INTO advertisement (type, text, actual_until) VALUES ('Advertisement', '{text}', "
                         f"'{actual_until}')")                                                                          #insert data into the table
        self.conn.commit()

    def write_to_vacancy(self, position, text, salary, city, date):                                                     #function for writing into Vacancy data base
        with sqlite3.connect(self.connection_string) as self.conn:
            self.cur = self.conn.cursor()
            print("Connection to SQLite DB successful")
        news_table = self.cur.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' 
        AND name='vacancy' ''')                                                                                         #verification existing table in DB
        if news_table.fetchone()[0] == 1:
            pass
        else:
            self.cur.execute('CREATE TABLE vacancy (type varchar(50), position varchar(100), text varchar(250), '
                             'salary varchar(20), city varchar(100), date varchar(100))')                               #creating vacancy table
            print('Table was successfully created.')
        self.cur.execute(f"INSERT INTO vacancy (type, position, text, salary, city, date) VALUES "
                         f"('Vacancy', '{position}', '{text}', '{salary}', '{city}', '{date}')")                        #insert data into the table
        self.conn.commit()

