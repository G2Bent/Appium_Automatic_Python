from pymongo import MongoClient
import json
from pprint import pprint
import datetime

class MongoDB(object):
    def __init__(self):
        client = MongoClient('127.0.0.1', port=7101,
                             username='loltest', password='Lol@Test',
                             authSource='loltest', authMechanism='SCRAM-SHA-1')
        db = client.loltest
        # print(db)
        # 连接所用集合，也就是我们通常所说的表，test为表名
        self.collection = db.users

    def MongoFind_Phone(self,phone):
        try:
        # 查詢用戶是否存在
            result = self.collection.find_one({'mobile': phone})
            # token_str = result.text
            # token_dict = json.dumps(result['mobile'])
            if result == None:
                return result
            else:
                return result
        except:
            raise Exception


    def MongoFind_NickName(self,name):
        try:
            # 查詢用戶是否存在
            result = self.collection.find_one({'nickname': name})
            # token_str = result.text
            # token_dict = json.dumps(result['nickname'])
            if result == None:
                return result
            else:
                return result
        except:
            raise Exception

    def MongoDele_Phone(self,phone):
        try:
            # 對已存在用戶進行刪除
            self.collection.remove({'mobile': phone})
            # MongoFind_Phone(phone)
            result_find = self.collection.find_one({'mobile': phone})
            # token_dict = json.dumps(result_find['mobile'])
            if result_find == None:
                return result_find
            else:
                return result_find
        except:
            raise Exception

    def MongoDele_Nickname(self,name):
        try:
            # 對已存在用戶進行刪除
            self.collection.delete_one({'nickname': name})
            # MongoFind_NickName(name)
            result_find = self.collection.find_one({'nickname': name})
            # token_dict = json.dumps(result_find['nickname'])
            if result_find == None:
                return result_find
            else:
                return result_find
        except:
            raise Exception

    def MongoInsert_User(self,nickname, mobile):
        try:
            result = self.collection.insert_one({"nickname": nickname, "mobile": mobile})
            result_find = self.collection.find_one({'nickname': nickname})
            token_dict = json.dumps(result_find['nickname'])
            if result == None:
                return token_dict
            else:
                return token_dict
        except:
            raise Exception

if __name__ =="__main__":
    test = MongoDB()
    print(test.MongoFind_NickName('erictsang7'))
    print(test.MongoFind_NickName('66566555555'))
    print(test.MongoDele_Nickname('test2028'))
    print(test.MongoDele_Phone('7889565655'))
    print(test.MongoInsert_User('test2028','7889565655'))
