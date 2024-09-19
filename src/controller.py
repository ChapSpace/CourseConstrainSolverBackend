from flask import Flask, jsonify, request
from classes.constrain.program import Program
from classes.constrain.profile import Profile
from classes.solver_config import SolverConfig
from pymongo import MongoClient
from classes.components.course import Course
from classes.components.enums import Quarter
import json


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
    
    # Extracting URL parameters
    program_id = request.args.get("program")
    profile_id = request.args.get("profile")
    
    # Accessing collections
    db = client["SchedulerDB"]
    program_collection = db["Programs"]
    profile_collection = db["Profiles"]
    
    # TODO: Add null checking
    # Pulling documents
    program_dict = program_collection.find_one({"id": program_id})
    profile_dict = profile_collection.find_one({"id": profile_id})
    
    # Converting to objects
    program_obj = Program.from_dict(program_dict)
    profile_obj = Profile.from_dict(profile_dict)
    
    # TODO: Add validation to objects (most immediately course) to make sure they have necessary fields
    # Configuring solver
    scheduleSolver = SolverConfig(program=program_obj, profile=profile_obj)
    
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
    db = client["SchedulerDB"]
    collection = db["Programs"]
    
    # Pseudo validation (Add real validation)
    request_json = request.json
    program = Program.from_dict(request_json)
    program_insert = program.to_dict()
    
    inserted_id = collection.insert_one(program_insert).inserted_id
    inserted_string = f"Inserted ID: {inserted_id}"
    
    return jsonify({"result": inserted_string}), 200

@app.post('/post-profile')
def post_profile():
    
    # Accessing DB and collection
    db = client["SchedulerDB"]
    collection = db["Profiles"]
    
    # Pseudo validation (Add real validation)
    request_json = request.json
    profile = Profile.from_dict(request_json)
    profile_insert = profile.to_dict()
    
    inserted_id = collection.insert_one(profile_insert).inserted_id
    inserted_string = f"Inserted ID: {inserted_id}"
    
    return jsonify({"result": inserted_string}), 200

app.run(debug=True)
    