from abc import ABCMeta, abstractmethod
from pymongo import MongoClient
# from MistTrigger import deviceTrigger

class db(object):
    __metaclass__ = ABCMeta
    @abstractmethod
    def getDefault(self):
        pass
    
    @abstractmethod
    def trigger(self):
        pass

    def __init__(self, dbName):
        self.__dbName = dbName
        self.__connect()

    def __connect(self):

        self.__client = MongoClient()
        self.__db = self.__client[self.__dbName]
        self.__device = self.__db.device

        if self.__device.count() != 1:
            self.__reset()

    def __reset(self):
        try:
            self.__db.deleteMany({})
        except:
            pass

        self.__device.insert(self.getDefault())

    def getProp(self, prop):
        return self.__device.find_one()[prop]

    def setProp(self, prop, value):
        self.trigger()
        return self.__device.update({}, {prop: value})

    

class dbDevice(db):

    def __init__(self):
        db.__init__(self, 'mistlogic')

    def getDefault(self):
        return {
            'manual': False,
            'auto': False,
            'password': "f36569537d40464df7dab6fb4aae6819"
        }

    def trigger(self):
        # deviceTrigger({'manual': self.getProp('manual')})
        pass
        
class dbNet(db):

    def __init__(self):
        db.__init__(self, 'netconf')

    def getDefault(self):
        return {
            'ip': "192.168.1.1",
            'ap': True,
            'netmask': "255.255.255.0",
            'dhcp': True,
            'ssid': "",
            'passphrase': ""
        }

    def trigger(self):
        pass

