import re
import metaData


class User(metaData.Data):


    def inputEmail(self):
        '''
        To check authentic mail address
        VIA regex
        '''
        while True:
            email = input("Enter your email address :")
            EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")
            if not EMAIL_REGEX.match(email):
                print("invalid mail address!!!")
            else:
                return email


    def login(self):
        self.name = input("Enter your name : ")          #asks for name
        self.email = self.inputEmail()

        self.insertUser((self.userCount() + 1, self.name, self.email))         #inserts to DB
        self.updateUser()


    def saveData(self):
        self.DB.commit()


user1 = User()        #creates user instance
user1.login()         #to login
user1.saveData()          #to save data

        #saves all commit
