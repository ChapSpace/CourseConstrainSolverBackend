from classes.solver_config import SolverConfig
from classes.constrain.program import Program
from classes.constrain.profile import Profile
from classes.components.course import Course
from classes.components.enums import Quarter

def main():
    
    # Arranging constraint objects
    degreeProgram = Program(required_courses=[Course(code='C1', units=5, offered_quarters=[Quarter.FALL]),
                            Course(code='C2', units=5, offered_quarters=[Quarter.WINTER]),
                            Course(code='C3', units=5, offered_quarters=[Quarter.SPRING]),
                            Course(code='C4', units=5, offered_quarters=[Quarter.SUMMER])])
    constrainProfile = Profile(max_quarter_units=5)

    # Creating and configuring solver
    scheduleSolver = SolverConfig(program=degreeProgram, profile=constrainProfile)
    scheduleSolver.add_required_courses_constraints()
    scheduleSolver.add_quarter_load_constraints()
    
    # Solving
    scheduleSolver.solve_constraints()

    

if __name__ == '__main__':
    main()