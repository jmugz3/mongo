
import pymongo
import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the school database
db=connection.school
scores = db.scores  #scores is the collection


def find():

    print "find, reporting for duty"

    query = {'type':'exam'}

    try:
        #multiple doc return, so use cursor
        cursor = scores.find(query)

    except Exception as e:
        print "Unexpected error:", type(e), e

    sanity = 0
    for doc in cursor:
        print doc
        sanity += 1
        if (sanity > 10):
            break
        


def find_one():

    print "find one, reporting for duty"
    query = {'student_id':10}
#   query2 = { }
#   query3 = {'type':'quiz', 'score':{'$gt':20, '$lt':90}}
    
    try:
        #each of the driver name methods depending on the language
        #Check CRUD spec
        doc = scores.find_one(query)
        
    except Exception as e:
        print "Unexpected error:", type(e), e

    
    print doc


find()
#find_one()

