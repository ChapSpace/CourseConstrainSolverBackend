from flask import Flask, jsonify, request
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


# Insert a program document into DB
@app.post('/post-program')
def post_program():
    
    # Accessing DB and collection
    db = client.test_DB
    collection = db.test_collection
    
    request_json = request.json
    program = Program.from_dict(request_json)
    program_insert = program.to_dict()
    
    inserted_id = collection.insert_one(program_insert).inserted_id
    inserted_string = f"Inserted ID: {inserted_id}"
    
    return jsonify({"result": inserted_string}), 200

app.run(debug=True)
    