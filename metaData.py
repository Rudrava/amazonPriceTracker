import databaseManager
import json


class Data(databaseManager.Database):

    data = {}

    def __init__(self):
        self.inititalize()
        with open("metaData.json", "r") as file:
            self.data = json.load(file)


    def save(self):
        with open("metaData.json", "w") as file:
            json.dump(self.data, file, indent = 4)

    def commitData(self):
        self.DB.commit()


    def updateProduct(self):
        self.pointer.execute('select count(*) from products where user_id = '+str(self.data["user_id"])+';')
        (ret,) = self.pointer
        self.data['noProducts'] = ret[0]
        self.save()


    def updateUser(self):
        self.pointer.execute('select count(*) from userdetails;')
        (ret,) = self.pointer
        self.data['noUsers'] = ret[0]
        self.save()


    def switchUser(self, uId):
        if uId <= self.data["noUsers"]:
            self.data["user_id"] = uId
            self.save()
            self.updateAll()


    def updateAll(self):
        self.updateProduct()
        self.updateUser()


    def productCount(self):
        return self.data['noProducts']


    def userCount(self):
        return self.data['noUsers']


    def storeData(self, link):
        # global count
        page = requests.get(link, headers = Product.headers)

        soup = BeautifulSoup(page.content, "html.parser")

        self.title = soup.find(id="productTitle").text.strip()[:20]
        self.price = self.toInt(soup.find(id="priceblock_ourprice").get_text())
        print(self.title, "\nCOSTS:- ",self.price)
        self.insertProduct((self.productCount() + 1, self.title, link[0:20], self.price))
        self.updateProduct()

# metaData = Data()
# metaData.updateProduct()
# metaData.updateUser()
# metaData.updateProduct()

# print(metaData.productCount(), metaData.userCount())


