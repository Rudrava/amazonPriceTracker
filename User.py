import re
import requests
import time
from bs4 import BeautifulSoup
from databaseManager import *
# from product import Product


class User(Database):

    headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'
}

    def toInt(self, string):
        string.split()
        number = ""
        for letter in string:
            if letter not in ('₹',','):
                if letter != '.':
                    number += letter
                else:
                    return int(number)


    def fetchData(self, link):
        # global count
        try:
            page = requests.get(link, headers = self.headers)
        except requests.exceptions.HTTPError:
            print("invalid Link!!!")
            time.sleep(1)
        soup = BeautifulSoup(page.content, "html.parser")
        try:
            self.title = soup.find(id="productTitle").text.strip()[:20]
        except:
            print("Product not available !!!")
            time.sleep(1)
            return
        try:
            self.price = self.toInt(soup.find(id="priceblock_ourprice").get_text())
        except:
            print("may be out of stock")
            self.price = 'N/A'
            time.sleep(1)
        print('Product Name:- ',self.title, "\nCOSTS:- ",self.price)
        self.updateProductCount()
        self.insertProduct((self.data['user_id'],self.data['noProducts'] + 1, self.title, link[0:20], self.price))
        self.commitData()
        time.sleep(2)


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
        self.connect()
        self.localeDatainitiate()
        self.updateUserCount()
        self.newUser((self.data['noUsers'] + 1, self.name, self.email))         #inserts to DB
        self.commitData()


    def signIn(self):
        self.name = input("Enter your name : ")          #asks for name
        self.connect()
        uId = self.oldUser(self.name)
        # print(uId)
        if uId:
            self.localeDatainitiate()
            self.data['user_id'], self.data['userName'] = uId, self.name
            return True
        else:
            # print("U dont seem to use our services")
            return False
        # self.updateProduct()
        # print(self.data['noProducts'])


# user1 = User()        #creates user instance
# # # user1.login()     #to login
# user1.signIn()     #to login
# user1.fetchData("https://www.amazon.in/gp/product/B078BNQ318/ref=s9_acss_bw_cg_oneplus_2a1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-3&pf_rd_r=JR4XRHAK8ZYR55591ENN&pf_rd_t=101&pf_rd_p=6ea832c7-9954-443c-b4cf-c62faba53ec6&pf_rd_i=21439725031")
# user1.productList()
