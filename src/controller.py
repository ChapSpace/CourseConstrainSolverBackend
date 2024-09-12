from flask import Flask, jsonify
from classes.constrain.program import Program
from classes.constrain.profile import Profile
from classes.solver_config import SolverConfig
from pymongo import MongoClient

# Mock database
from mock_db import MockDB

# Database testing
connection_string = "mongodb+srv://ericcui:a3tgSg0tVBJ9bhg5@cluster0.r6ela.mongodb.net/"
client = MongoClient(connection_string)

db = client.test_DB
collection = db.test_collection

user_document = {
    "username": "john_doe",
    "email": "john.doe@example.com",
    "age": 28
}

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
    scheduleSolver.add_required_courses_constraints()
    scheduleSolver.add_quarter_load_constraints()
    
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
    
    inserted_id = collection.insert_one(user_document).inserted_id
    inserted_string = f"Inserted ID: {inserted_id}"
    
    return jsonify({"result": inserted_string}), 200
    

app.run(debug=True)
    