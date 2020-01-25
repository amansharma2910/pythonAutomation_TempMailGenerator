# The OS module allows us to perform operating system dependant functionalities.
import os
# The webbrowser module allows us to perform browser operations such as opening a website, which is what we are going to do using this script.
import webbrowser
# The date method of datetime module allows us to get the date on which the tempmail was generated.
from datetime import date as dt
# The string and random modules will help us generate a password.
import random

class TempmailGen:

# This is the initializer method for the class.
    def __init__(self, website = "", tempmail = "asada1920@gmail.com", password = "adadadafgf", date = ""):
        self.website = website
        self.tempmail = tempmail
        self.password = password
        self.date = date
    
# With this, we define the getter for the "website" parameter.
    @property
    def website(self):
        return self.__website

# Setter for inputting the name of website you want to generate the tempmail for.
    @website.setter
    def website(self, website):
        website = input("Enter the name of the website you want to generate the tempmail for: ")
        self.__website = website
# With this, we define the getter for the "website" parameter.

    @property
    def date(self):
        return self.__date

# Setter for inputting the name of website you want to generate the tempmail for.
    @date.setter
    def date(self, date):
        date = dt.today().strftime("%d/%m/%Y")
        self.__date = date
    
# The following code block will open the tempmail website for you.
    def tempmailOpener(self):
        url = 'https://temp-mail.org/en/'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open_new(url)

# The following code block will add the generated tempmail, password and website name to the "passwords.txt" file.
    def passwordManager(self):
        with open("passwords.txt", mode = "a", encoding = "utf-8") as my_file:
            my_file.write("\n\nDATE: {}\nWEBSITE: {}\nTEMPMAIL: {}\nPASSWORD: {}".format(self.date, self.website, self.tempmail, self.password))

    def passwordGenerator(self):
        key = self.tempmail
        self.password = "".join(random.choice(key) for i in range(9)) + "@"


    def __str__(self):
        return "{}".format(self.date)


def main():
    test = TempmailGen()
    test.tempmailOpener()
    test.passwordGenerator()
    test.passwordManager()
    print(test)

main()