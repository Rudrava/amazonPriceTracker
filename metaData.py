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


    def updateProduct(self):
        self.pointer.execute('select count(*) from products;')
        (ret,) = self.pointer
        self.data['noProducts'] = ret[0]
        self.save()


    def updateUser(self):
        self.pointer.execute('select count(*) from userdetails;')
        (ret,) = self.pointer
        self.data['noUsers'] = ret[0]
        self.save()


    def updateAll(self):
        self.updateProduct()
        self.updateUser()


    def productCount(self):
        return self.data['noProducts']


    def userCount(self):
        return self.data['noUsers']



# metaData = Data()
# metaData.save()
# metaData.updateUser()
# metaData.updateProduct()

# print(metaData.productCount(), metaData.userCount())


