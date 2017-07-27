from pymongo import MongoClient

class Config(object):

    def __init__(self, name, default):
        self.__name = name
        self.__default = default
        self.__connect()

    def __connect(self):

        client = MongoClient()
        db = client["mistlogic"]

        self.__collection = db[self.__name]

        if self.__collection.count() != 1:
            self.__reset()

    def __reset(self):
        try:
            self.__collection.deleteMany({})
        except:
            pass

        self.__collection.insert(self.__default)

    def getProp(self, prop):
        return self.__collection.find_one()[prop]

    def setProp(self, prop, value):
        props = self.__collection.find_one()
        props[prop] = value
        return self.__collection.update({}, props)

