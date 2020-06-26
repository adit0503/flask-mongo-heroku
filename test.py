from pymongo import MongoClient

client = MongoClient("mongodb+srv://qxqt:aditya1234@cluster-demo-weusg.mongodb.net/gita?retryWrites=true&w=majority")
gita = client["gita"]
shloka = gita["shloka"]

shloka.delete_many({})
