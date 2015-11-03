import pymongo
from bson.son import SON

connection = pymongo.MongoClient("mongodb://localhost")

db = connection.school
school = db.students
pipeline = {}


pipeline.update(
    {"$unwind": "$scores"},
    {"$match": {"scores.type":"homework"}},
    {"$group": {"_id":"$_id","score": {"$min" : "$scores.score"}},
    {"$sort": {"$scores.score":1}}
)


print list(school.aggregate(pipeline))

# In the Mongo Shell:
# db.students.aggregate(
#                         {'$unwind':  '$scores'}
#                         ,{'$match':  {'scores.type':'homework'}}
#                         ,{'$group':  {'_id':'$_id'
#                                     ,'score':'$scores.score'}}
#                         , {'$sort':  {"scores.score":1 }}
#                         ,{'$limit': 1}


#
# for i in result_set:
#     print i
#     print len(result_set)
