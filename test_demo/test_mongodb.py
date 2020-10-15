#!/usr/bin/python3

# import pymongo
#
# myclient = pymongo.MongoClient("mongodb://10.200.60.32:27017/")
# print(myclient.list_database_names())

from pymongo import MongoClient
from bson.objectid import ObjectId
from urllib.parse import quote_plus
a = str('a')

class TestMongo(object):

    def __init__(self):
        self.client = MongoClient("mongodb://10.200.60.32:27017/")
        self.db = self.client['students']

    def add_one(self):
        '''新增数据'''
        post ={
            'name': 'ben',
            'age': 18,
            'sex': "male",
            'grade': 80,
            'adress': "china"
        }
        return self.db.students.insert_one(post)
    def add_many(self):
        '''新增多条数据'''
        infos = [
            {'name': 'ben', 'age': 18, 'sex': "male", 'grade': 80, 'adress': "china"},
            {'name': 'sum', 'age': 19, 'sex': "male", 'grade': 75, 'adress': "china"},
            {'name': 'lily', 'age': 16, 'sex': "female", 'grade': 90, 'adress': "china"},
            {'name': 'teddy', 'age': 18, 'sex': "male", 'grade': 65, 'adress': "china"},
            {'name': 'fluence', 'age': 18, 'sex': "female", 'grade': 80, 'adress': "china"}
            ]
        return self.db.students.insert_many(infos)

    def get_one(self):
        '''查询一条数据'''
        return self.db.students.find_one()

    def get_more(self):
        '''查询多条数据'''
        return self.db.students.find({'age': 18})

    def get_one_from_oid(self, oid):
        '''查询指定ID的数据'''
        obj = ObjectId(oid)
        return self.db.students.find_one({'_id': obj})

    def update_one(self):
        '''修改一条数据'''
        return self.db.students.update_one({'age': 20}, {'$inc': {'x': 10}})

    def update_many(self):
        '''修改多条数据'''
        return self.db.students.update_many({}, {'$inc': {'age': 5}})

    def dalete_one(self):
        '''删除一条数据'''
        return self.db.students.delete_one({'name': 'ben'})

    def delete_many(self):
        '''删除多条数据'''
        return self.db.students.delete_many({'age': 24})


def main():
    obj = TestMongo()
    # rest = obj.add_one()
    # print(rest)
    #
    # rest = obj.add_many()
    # print(rest)
    #
    # rest = obj.get_one()
    # print(rest)

    rest = obj.get_more()
    for i in rest:
        print(i['_id'])

    # rest = obj.get_one_from_oid('5c68b5cb5a49891b40b8a18e')
    # print(rest)
    #
    # rest = obj.update_one()
    # print(rest)
    #
    # rest = obj.update_many()
    # print(rest)

    # rest = obj.delete_one()
    # print(rest.delete_count)
    #
    # rest = obj.delete_many()
    # print(rest.delete_count)


if __name__ == '__main__':
    main()

