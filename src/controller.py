from flask import Flask, jsonify
from classes.constrain.program import Program
from classes.constrain.profile import Profile
from classes.solver_config import SolverConfig
from pymongo import MongoClient
from classes.components.course import Course
from classes.components.enums import Quarter
import json

# Mock database
from mock_db import MockDB

def load_app_settings(file_path='appsettings.json'):
    with open(file_path, 'r') as file:
        app_settings = json.load(file)
        return app_settings
    
# Database testing
app_settings = load_app_settings()
connection_string = app_settings["DatabaseConnection"]["ConnectionString"]
client = MongoClient(connection_string)


app = Flask(__name__)

@app.get('/solve-user-schedule')
def solve_user_schedule():
    
    # Initialize mock database
    database = MockDB()
    
    # Pulling data from mock database
    degreeProgram = database.program
    constrainProfile = database.profile
    
    # Configuring solver
    scheduleSolver = SolverConfig(program=degreeProgram, profile=constrainProfile)
    
    # Solving and creating output
    schedule = scheduleSolver.solve()
    scheduleString = ""
    if schedule:
        for course_code, quarter in schedule.items():
            scheduleString += f" | {course_code} is scheduled for {quarter}"
    else:
        scheduleString = "No valid schedule found"
    
    # Returning
    return jsonify({"schedule": scheduleString}), 200


@app.post('/post-test')
def post_test():
    
    # Accessing DB and collection
    db = client.test_DB
    collection = db.test_collection
    
    # Setting up classes
    C1 = Course(code='C1', units=5, offered_quarters=[Quarter.FRESH_FALL])
    C2 = Course(code='C2', units=5, offered_quarters=[Quarter.FRESH_WINTER])
    C3 = Course(code='C3', units=5, offered_quarters=[Quarter.FRESH_SPRING])
    C4 = Course(code='C4', units=5, offered_quarters=[Quarter.FRESH_SUMMER])
    
    program = Program(required_courses=[C1, C2, C3, C4])
    program_insert = program.to_dict()
    
    inserted_id = collection.insert_one(program_insert).inserted_id
    inserted_string = f"Inserted ID: {inserted_id}"
    
    return jsonify({"result": inserted_string}), 200

app.run(debug=True)
    