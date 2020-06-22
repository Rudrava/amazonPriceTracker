import mysql.connector
import json

class Database():

    data = {}

    def connect(self):
        """
        This creates a connection to the DB hosted in localhost
        and returns the pointer to the connection class and the cursor method

        This would be initialized from sign in method if user eexists

        """
        try:
            Db = mysql.connector.connect(user='root', password='Rudra1@sql',
                                  host='127.0.0.1',
                                      database='amazonPriceTracker')
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

        # print("Connected")
        self.DB, self.pointer = (Db, Db.cursor())


    def localeDatainitiate(self):
        '''
        saves locale data to storage
        TO BE INVOKED BY SIGN IN and login for fast
        data access
        '''
        with open("metaData.json", "r") as file:
            self.data = json.load(file)



    def insertProduct(self, data):
        '''
        inserts data into DB
        '''
        cmd = 'insert into products (user_id, product_id, productName, productLink, price) values (%s, %s, %s, %s, %s)'
        self.pointer.execute(cmd, data)
        self.updateProductCount()


    def updateProductCount(self):
        '''
        updates user product data from DB to locale data
        '''
        self.pointer.execute('select count(*) from products where user_id = '+str(self.data["user_id"])+';')
        (ret,) = self.pointer
        self.data['noProducts'] = ret[0]




    def newUser(self, data):
        '''
        creates a new user into db
        TO BE INVOLED BY LOGIN METHOD
        '''
        cmd = 'INSERT INTO userdetails (user_id, name, eMail) values(%s, %s, %s)'
        self.pointer.execute(cmd, data)


    def oldUser(self, name):
        '''
        to check if user exists returns userID
        to be invoked by signin method
        '''
        cmd = 'select user_id from userdetails where name = "'+name+'";'
        self.pointer.execute(cmd)

        try:
            (ret,) = self.pointer
            return ret[0]
        except ValueError:
            return False


    def updateUserCount(self):
        self.pointer.execute('select count(*) from userdetails;')
        (ret,) = self.pointer
        self.data['noUsers'] = ret[0]


    def productList(self):
        '''
        Prinits the productsName and Price'''
        cmd = "select productName, price from products where user_id = "+str(self.data['user_id'])+""
        self.pointer.execute(cmd)
        for returnVal in self.pointer:
            print(returnVal[0], '\t\t\t\t\t\t',returnVal[1])


    def commitData(self):
        self.DB.commit()
