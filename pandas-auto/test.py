from pymongo import MongoClient
import numpy as np
import pandas as pd
cluster = MongoClient("mongodb+srv://qxqt:aditya1234@cluster-demo-weusg.mongodb.net/gita?retryWrites=true&w=majority")
gita = cluster["gita"]
shloka = gita["shloka"]

'''
df = pd.read_csv("bhagavad-gita.csv")
df.drop(df.columns[[0,3,4]], axis=1, inplace=True)
L = []
for i,r in df.iterrows():
    L.append('BG' + str(r['title']).replace('.',''))
lset = set()
for i,l in enumerate(L):
    if l in lset:
        L[i] = l+'0'
    else:
        lset.add(l)
df.insert(2,"id",L)
# df2.to_csv("output.csv")

for i,r in df.iterrows():
    s = {"_id":r["id"],"text":r["devanagari"]}
    shloka.insert_one(s)
'''

# .insert_many() .insert_one()
# post = {"_id":10,"name":"adity"}
# collection.insert_one(post)

# for i in range(10,20):
#     post = {"_id":i,"name":"svojwfewf","loc":"wiiuwfv"}
#     collection.insert_one(post)

# .find()  .find_one()
# result = collection.find({})
# for r in result:
#     print(r["text"])

#.delete_one()
# result = collection.delete_one({"_id":4})
shloka.delete_many({})
