import mysql.connector


class Database():

    def inititalize(self):
        self.DB, self.pointer = self.connect()


    def connect(self):
        """
        This creates a connection to the DB hosted in localhost
        and returns the pointer to the connection class and the cursor method
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

        print("COnnected")
        return (Db, Db.cursor())


    def insertProduct(self, data):
        cmd = 'insert into products (user_id, product_id, productName, productLink, price) values (%s, %s, %s, %s, %s)'
        self.pointer.execute(cmd, data)


    def insertUser(self, data):
        cmd = 'INSERT INTO userdetails (user_id, name, eMail) values(%s, %s, %s)'
        self.pointer.execute(cmd, data)


    def userPresent(self, name):
        cmd = 'select user_id from userdetails where name = "'+name+'";'
        self.pointer.execute(cmd)

        try:
            (ret,) = self.pointer
            return ret[0]
        except ValueError:
            return False


    def status(self):
        cmd = "select productName, price from products where user_id = "+str(self.data['user_id'])+""
        self.pointer.execute(cmd)
        for returnVal in self.pointer:
            print(returnVal[0], returnVal[1])
