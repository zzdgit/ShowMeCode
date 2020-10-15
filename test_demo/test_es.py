# from elasticsearch5 import Elasticsearch
#
# ES = [
#     '10.200.64.50:9200'
# ]
#
#
# es = Elasticsearch(
#     ES,
#     sniff_on_start=True,
#     sniff_on_connection_fail=True,
#     sniffer_timeout=60
# )
#
# query = {"query":{"match_all":{}}}
# ret = es.search(index='ld.case.rule.20190630.other', doc_type='esbasejudgement', body=query)
#
# print(ret)
#
#
# class sigle()
#
#     def __new__(cls, *args, **kwargs):
#         if cls.instance:
#             return cls.instance
#         return cls.
#
#
# fn = lambda x : fn(n-1) + f(n-2)
# import json
# import requests
#
# #url = 'http://10.202.41.81:8998/sessions'
# url = 'http://10.202.41.219:8999/sessions'
# param = {'from': 2,
#          'size': 10}
# result = requests.get(url, params=param)
# data = json.loads(result.content.decode())
# print(data)



# -*- coding: utf-8 -*-

import os
import shutil
#
# file_dir = './tmp'
# new_dir = './new_tmp'
#
# for root, dirs, files in os.walk(file_dir):
#     print(root) #当前目录路径
#     print(dirs) #当前路径下所有子目录
#     print(files) #当前路径下所有非目录子文件
#     for dir in dirs:
#         # 创建新的文件夹
#         tar_dir = dir.replace('+', '')
#         target = os.path.join(new_dir, tar_dir)
#         os.makedirs(target)
#         for file in files:
#             srcFile = os.path.join(root, file)
#             tar_file = file.replace('+', '')
#             dstFile = os.path.join(target, tar_file)
#             try:
#                 shutil.copy(srcFile, dstFile)
#             except IOError as e:
#                 print("Unable to copy file. %s" % e)



file_dir = './tmp'

for root, dirs, files in os.walk(file_dir):
    for dir in dirs:
        # 创建新的文件夹
        tar_dir = dir.replace('+', '')
        target = os.path.join(root, tar_dir)
        target.replace('+', '')
        if not os.path.isdir(target):
            os.makedirs(target)
    for file in files:
        srcFile = os.path.join(root, file)
        dstFile = srcFile.replace('+', '')
        try:
            shutil.copy(srcFile, dstFile)
            print("重命名已完成： {0}".format(srcFile))
        except IOError as e:
            print("Unable to copy file. {0}".format(srcFile))
