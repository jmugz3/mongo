import pymongo
import sys

# connnecto to the db on standard port
connection = pymongo.MongoClient("mongodb://localhost")

#removes homework grades
def remove_grade(grade_type):

    #handles
    db = connection.students
    scores = db.grades

    try:

        scores.aggregate({$group:{'_id':}})


        result = scores.delete_many({'type':grade_type})

        print "num removed: ", result.deleted_count


    except Exception as e:
        print "Exception: ", type(e), e


##def find_student_data():
##
##    #handles
##    db = connection.students
##    scores = db.grades
##
####    print "Searching for student data for student with id = " 
##
##    try:
##
##        docs = scores.find().sort( { 'score' : -1 } ).skip( 100 ).limit( 1 )
####        for doc in docs:
####            print doc
##
##    except Exception as e:
##        print "Exception: " , type(e), e


remove_grade("homework")
#find_student_data()

    
