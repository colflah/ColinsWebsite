import pymongo


connection = pymongo.MongoClient("mongodb://colflah:9A8-EXQ-xzY-FUF@ds123331.mlab.com:23331/colinandcamilleswebsitemailinglist")
db = connection["colinandcamilleswebsitemailinglist"]
collection2 = db['test']
collection2.insert_one({'this is another': 'test'})
for test in collection2.find():
	print test
