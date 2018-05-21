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
        # 查村用戶是否存在
        result = self.collection.find_one({'mobile': phone})
        # token_str = result.text
        # token_dict = json.dumps(result['mobile'])
        if result == None:
            print("用户不存在")
        else:
            print("用户存在:")
        return True

    def MongoFind_NickName(self,name):
        # 查村用戶是否存在
        result = self.collection.find_one({'nickname': name})
        # token_str = result.text
        # token_dict = json.dumps(result['nickname'])
        if result == None:
            print("用户不存在")
        else:
            print("用户存在")
        return True

    def MongoDele_Phone(self,phone):
        # 對已存在用戶進行刪除
        self.collection.remove({'mobile': phone})
        # MongoFind_Phone(phone)
        result_find = self.collection.find_one({'mobile': phone})
        # token_dict = json.dumps(result_find['mobile'])
        if result_find == None:
            print("用户已刪除")
        else:
            print("用戶未刪除")
        return True

    def MongoDele_Nickname(self,name):
        # 對已存在用戶進行刪除
        self.collection.delete_one({'nickname': name})
        # MongoFind_NickName(name)
        result_find = self.collection.find_one({'nickname': name})
        # token_dict = json.dumps(result_find['nickname'])
        if result_find == None:
            print("用户已刪除:")
        else:
            print("用戶未刪除:")
        return True

    def MongoInsert_User(self,nickname, mobile):
        result = self.collection.insert_one({"nickname": nickname, "mobile": mobile})
        result_find = self.collection.find_one({'nickname': nickname})
        token_dict = json.dumps(result_find['nickname'])
        if result == None:
            print("用戶插入失敗")
        else:
            print("用戶插入成功")
        return True

