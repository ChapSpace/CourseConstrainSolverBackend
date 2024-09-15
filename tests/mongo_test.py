import mongomock
from classes.components.course import Course
from classes.components.enums import Quarter

def test_simple_course_insert():
    mock_client = mongomock.MongoClient()
    mock_database = mock_client["test_DB"]
    mock_collection = mock_database["test_collection"]
    
    course = Course(code="Code",units=5)
    course_insert = course.to_dict()
    
    result = mock_collection.insert_one(course_insert)
    assert result != None
    
    
    
    