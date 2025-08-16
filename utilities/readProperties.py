import configparser
import os

config=configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir)+'\\configurations\\config.ini')

class ReadConfig():
    @staticmethod
    def getApplicationURL():
        url=config.get('common','base_url')
        return url

    def getMobileNumber(self):
        mobile=config.get('credentials','mobile')
        return mobile
    def getUserName(self):
        userName=config.get('credentials','username')
        return userName
    def getPassword(self):
        password=config.get('credentials','password')
        return password