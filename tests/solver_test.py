from classes.solver_config import SolverConfig
from classes.constrain.program import Program
from classes.constrain.profile import Profile
from classes.components.course import Course
from classes.components.enums import Quarter
from z3 import sat, unsat


def test_add_required_courses_constraints_sat():
    
    degreeProgram = Program(
        required_courses=[
            Course(code='C1', units=5, offered_quarters=[Quarter.FALL]),
            Course(code='C2', units=5, offered_quarters=[Quarter.WINTER]),
            Course(code='C3', units=5, offered_quarters=[Quarter.SPRING]),
            Course(code='C4', units=5, offered_quarters=[Quarter.SUMMER]),
        ]
    )
    
    # Creating and configuring solver
    scheduleSolver = SolverConfig(program=degreeProgram)
    scheduleSolver.add_required_courses_constraints()
    
    assert scheduleSolver.check_solvable() == sat
    
def test_add_required_courses_constraints_one_per_quarter_sat():
    
    degreeProgram = Program(
        required_courses=[
            Course(code='C1', units=5, offered_quarters=[Quarter.FALL]),
            Course(code='C2', units=5, offered_quarters=[Quarter.WINTER]),
            Course(code='C3', units=5, offered_quarters=[Quarter.SPRING]),
            Course(code='C4', units=5, offered_quarters=[Quarter.SUMMER]),
        ]
    )
    
    constrainProfile = Profile(max_quarter_units=5)
    
    # Creating and configuring solver
    scheduleSolver = SolverConfig(program=degreeProgram, profile=constrainProfile)
    scheduleSolver.add_required_courses_constraints()
    scheduleSolver.add_quarter_load_constraints()
    
    assert scheduleSolver.check_solvable() == sat
    
def test_add_required_courses_constraints_one_per_quarter_unsat():
    
    degreeProgram = Program(
        required_courses=[
            Course(code='C1', units=5, offered_quarters=[Quarter.FALL]),
            Course(code='C2', units=5, offered_quarters=[Quarter.WINTER]),
            Course(code='C3', units=5, offered_quarters=[Quarter.SPRING]),
            Course(code='C4', units=5, offered_quarters=[Quarter.SUMMER]),
        ]
    )
    
    constrainProfile = Profile(max_quarter_units=4)
    
    # Creating and configuring solver
    scheduleSolver = SolverConfig(program=degreeProgram, profile=constrainProfile)
    scheduleSolver.add_required_courses_constraints()
    scheduleSolver.add_quarter_load_constraints()
    
    assert scheduleSolver.check_solvable() == unsat

def test_add_required_courses_constraints_multiple_per_quarter_sat():
    
    degreeProgram = Program(
        required_courses=[
            Course(code='C1', units=5, offered_quarters=[Quarter.FALL]),
            Course(code='C2', units=5, offered_quarters=[Quarter.WINTER]),
            Course(code='C3', units=5, offered_quarters=[Quarter.SPRING]),
            Course(code='C4', units=5, offered_quarters=[Quarter.SUMMER]),
            Course(code='C5', units=5, offered_quarters=[Quarter.FALL]),
            Course(code='C6', units=5, offered_quarters=[Quarter.WINTER]),
            Course(code='C7', units=5, offered_quarters=[Quarter.SPRING]),
            Course(code='C8', units=5, offered_quarters=[Quarter.SUMMER]),
        ]
    )
    
    constrainProfile = Profile(max_quarter_units=10)
    
    # Creating and configuring solver
    scheduleSolver = SolverConfig(program=degreeProgram, profile=constrainProfile)
    scheduleSolver.add_required_courses_constraints()
    scheduleSolver.add_quarter_load_constraints()
    
    assert scheduleSolver.check_solvable() == sat
    
def test_add_required_courses_constraints_multiple_per_quarter_unsat():
    
    degreeProgram = Program(
        required_courses=[
            Course(code='C1', units=5, offered_quarters=[Quarter.FALL]),
            Course(code='C2', units=5, offered_quarters=[Quarter.WINTER]),
            Course(code='C3', units=5, offered_quarters=[Quarter.SPRING]),
            Course(code='C4', units=5, offered_quarters=[Quarter.SUMMER]),
            Course(code='C5', units=5, offered_quarters=[Quarter.FALL]),
            Course(code='C6', units=5, offered_quarters=[Quarter.WINTER]),
            Course(code='C7', units=6, offered_quarters=[Quarter.SPRING]),
            Course(code='C8', units=5, offered_quarters=[Quarter.SUMMER]),
        ]
    )
    
    constrainProfile = Profile(max_quarter_units=10)
    
    # Creating and configuring solver
    scheduleSolver = SolverConfig(program=degreeProgram, profile=constrainProfile)
    scheduleSolver.add_required_courses_constraints()
    scheduleSolver.add_quarter_load_constraints()
    
    assert scheduleSolver.check_solvable() == unsat