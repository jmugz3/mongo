//in JavaScript
db.grades.aggregate([
        {'$match':{'score':{'$gte':65}}},
        {'$sort':{'score': 1}},
        {'$project': {'student_id':true ,'score':true, '_id':false}},
        {'$limit':1}])
