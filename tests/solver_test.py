from classes.solver_config import SolverConfig
from classes.constrain.program import Program
from classes.constrain.profile import Profile
from classes.components.course import Course
from classes.components.enums import Quarter
from z3 import sat, unsat


def test_add_required_courses_constraints_sat():
    degreeProgram = Program(
        required_courses=[
            Course(code='C1', units=5, offered_quarters=[Quarter.FRESH_FALL]),
            Course(code='C2', units=5, offered_quarters=[Quarter.FRESH_WINTER]),
            Course(code='C3', units=5, offered_quarters=[Quarter.FRESH_SPRING]),
            Course(code='C4', units=5, offered_quarters=[Quarter.FRESH_SUMMER]),
        ]
    )
    constrainProfile = Profile()

    # Creating and configuring solver
    scheduleSolver = SolverConfig(program=degreeProgram, profile=constrainProfile)
    
    assert scheduleSolver.check_solvable() == sat
    
def test_add_required_courses_constraints_one_per_quarter_sat():
    degreeProgram = Program(
        required_courses=[
            Course(code='C1', units=5, offered_quarters=[Quarter.FRESH_FALL]),
            Course(code='C2', units=5, offered_quarters=[Quarter.FRESH_WINTER]),
            Course(code='C3', units=5, offered_quarters=[Quarter.FRESH_SPRING]),
            Course(code='C4', units=5, offered_quarters=[Quarter.FRESH_SUMMER]),
        ]
    )
    
    constrainProfile = Profile(max_quarter_units=5)
    
    # Creating and configuring solver
    scheduleSolver = SolverConfig(program=degreeProgram, profile=constrainProfile)
    
    assert scheduleSolver.check_solvable() == sat
    
def test_add_required_courses_constraints_one_per_quarter_unsat():
    degreeProgram = Program(
        required_courses=[
            Course(code='C1', units=5, offered_quarters=[Quarter.FRESH_FALL]),
            Course(code='C2', units=5, offered_quarters=[Quarter.FRESH_WINTER]),
            Course(code='C3', units=5, offered_quarters=[Quarter.FRESH_SPRING]),
            Course(code='C4', units=5, offered_quarters=[Quarter.FRESH_SUMMER]),
        ]
    )

    constrainProfile = Profile(max_quarter_units=4)
    
    # Creating and configuring solver
    scheduleSolver = SolverConfig(program=degreeProgram, profile=constrainProfile)
    
    assert scheduleSolver.check_solvable() == unsat

def test_add_required_courses_constraints_multiple_per_quarter_sat():
    degreeProgram = Program(
        required_courses=[
            Course(code='C1', units=5, offered_quarters=[Quarter.FRESH_FALL]),
            Course(code='C2', units=5, offered_quarters=[Quarter.FRESH_WINTER]),
            Course(code='C3', units=5, offered_quarters=[Quarter.FRESH_SPRING]),
            Course(code='C4', units=5, offered_quarters=[Quarter.FRESH_SUMMER]),
            Course(code='C5', units=5, offered_quarters=[Quarter.FRESH_FALL]),
            Course(code='C6', units=5, offered_quarters=[Quarter.FRESH_WINTER]),
            Course(code='C7', units=5, offered_quarters=[Quarter.FRESH_SPRING]),
            Course(code='C8', units=5, offered_quarters=[Quarter.FRESH_SUMMER]),
        ]
    )
    
    constrainProfile = Profile(max_quarter_units=10)
    
    # Creating and configuring solver
    scheduleSolver = SolverConfig(program=degreeProgram, profile=constrainProfile)

    assert scheduleSolver.check_solvable() == sat
    
def test_add_required_courses_constraints_multiple_per_quarter_unsat():
    degreeProgram = Program(
        required_courses=[
            Course(code='C1', units=5, offered_quarters=[Quarter.FRESH_FALL]),
            Course(code='C2', units=5, offered_quarters=[Quarter.FRESH_WINTER]),
            Course(code='C3', units=5, offered_quarters=[Quarter.FRESH_SPRING]),
            Course(code='C4', units=5, offered_quarters=[Quarter.FRESH_SUMMER]),
            Course(code='C5', units=5, offered_quarters=[Quarter.FRESH_FALL]),
            Course(code='C6', units=5, offered_quarters=[Quarter.FRESH_WINTER]),
            Course(code='C7', units=6, offered_quarters=[Quarter.FRESH_SPRING]),
            Course(code='C8', units=5, offered_quarters=[Quarter.FRESH_SUMMER]),
        ]
    )
    
    constrainProfile = Profile(max_quarter_units=10)
    
    # Creating and configuring solver
    scheduleSolver = SolverConfig(program=degreeProgram, profile=constrainProfile)
    
    assert scheduleSolver.check_solvable() == unsat

def test_add_prerequisite_constraints_simple_sat():
    C1 = Course(code='C1', units=5, offered_quarters=[Quarter.FRESH_FALL, Quarter.FRESH_WINTER])
    C2 = Course(code='C2', units=5, offered_quarters=[Quarter.FRESH_FALL, Quarter.FRESH_WINTER])
    C3 = Course(code='C3', units=5, offered_quarters=[Quarter.FRESH_FALL, Quarter.FRESH_WINTER, Quarter.FRESH_SPRING], prereqs=[C1, C2])
    C4 = Course(code='C4', units=5, offered_quarters=[Quarter.FRESH_SPRING], prereqs=[C3])
    
    degreeProgram = Program(required_courses=[C1, C2, C3, C4])
    constrainProfile = Profile(max_quarter_units=20)
    
    # Creating and configuring solver
    scheduleSolver = SolverConfig(program=degreeProgram, profile=constrainProfile)
    
    assert scheduleSolver.check_solvable() == sat

def test_add_prerequisite_constraints_simple_unsat():
            
    C1 = Course(code='C1', units=5, offered_quarters=[Quarter.FRESH_FALL, Quarter.FRESH_WINTER])
    C2 = Course(code='C2', units=5, offered_quarters=[Quarter.FRESH_WINTER])
    C3 = Course(code='C3', units=5, offered_quarters=[Quarter.FRESH_WINTER], prereqs=[C1, C2])
    C4 = Course(code='C4', units=5, offered_quarters=[Quarter.FRESH_SPRING], prereqs=[C3])
    
    degreeProgram = Program(required_courses=[C1, C2, C3, C4])
    constrainProfile = Profile(max_quarter_units=20)
    
    # Creating and configuring solver
    scheduleSolver = SolverConfig(program=degreeProgram, profile=constrainProfile)
    
    assert scheduleSolver.check_solvable() == unsat

def test_changing_profile_max_quarter_units_sat_unsat():
    C1 = Course(code='C1', units=5, offered_quarters=[Quarter.FRESH_FALL, Quarter.FRESH_WINTER])
    C2 = Course(code='C2', units=5, offered_quarters=[Quarter.FRESH_FALL, Quarter.FRESH_WINTER])
    C3 = Course(code='C3', units=5, offered_quarters=[Quarter.FRESH_FALL, Quarter.FRESH_WINTER, Quarter.FRESH_SPRING], prereqs=[C1, C2])
    C4 = Course(code='C4', units=5, offered_quarters=[Quarter.FRESH_SPRING], prereqs=[C3])
    
    degreeProgram = Program(required_courses=[C1, C2, C3, C4])
    constrainProfile = Profile(max_quarter_units=20)
    
    # Creating and configuring solver
    scheduleSolver = SolverConfig(program=degreeProgram, profile=constrainProfile)
    
    assert scheduleSolver.check_solvable() == sat
    
    constrainProfile.max_quarter_units = 5
    
    assert scheduleSolver.check_solvable() == unsat