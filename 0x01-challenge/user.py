#!/usr/bin/python3
""" 
User class
"""

class User():
    """ Class that defines an user """

    def __init__(self):
        """ Constructor """
        self.__email = None

    @property
    def email(self):
        """ Getter of email attribute """
        return self.__email
    
    @email.setter
    def email(self, value):
        """ Setter of email attribute """
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value
   
    
if __name__ == "__main__":
    u = User()
    u.email = "john@snow.com"
    print(u.email)
