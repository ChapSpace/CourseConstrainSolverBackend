from flask import Flask, jsonify
from classes.constrain.program import Program
from classes.constrain.profile import Profile
from classes.solver_config import SolverConfig

# Mock database
from mock_db import MockDB

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
    

app.run(debug=True)
    