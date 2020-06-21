import re
import metaData
from product import Product

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


    def signIn(self):
        self.name = input("Enter your name : ")          #asks for name
        uId = self.userPresent(self.name)
        if uId:
            user1.switchUser(uId)
        else:
            print("You dont seem to use our services")
            exit()



user1 = User()        #creates user instance
# user1.login()     #to login
user1.signIn()     #to login
links = [
    "https://www.amazon.in/TP-Link-A5-Supports-Snooping-Streaming/dp/B07DYWS92W/ref=sr_1_5?dchild=1&keywords=tp+link+routers+5g&qid=1592655546&s=computers&sr=1-5",
    "https://www.amazon.in/gp/product/B078BNQ318/ref=s9_acss_bw_cg_oneplus_2a1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-3&pf_rd_r=JR4XRHAK8ZYR55591ENN&pf_rd_t=101&pf_rd_p=6ea832c7-9954-443c-b4cf-c62faba53ec6&pf_rd_i=21439725031",
    "https://www.amazon.in/Cosmic-Byte-GS410-Headphones-Green/dp/B07K7YR8SP/ref=lp_2591139031_1_4?s=videogames&ie=UTF8&qid=1592657539&sr=1-4"]

product =Product()

# f __name__ == "__main__":
for link in links:
    product.storeData(link)
    product.saveData()
# user1.status()
# user1.saveData()          #to save data

        #saves all commit
