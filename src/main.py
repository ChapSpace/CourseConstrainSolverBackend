from classes.solver_config import SolverConfig
from classes.constrain.program import Program
from classes.constrain.profile import Profile
from classes.components.course import Course
from classes.components.enums import Quarter

def main():
    
    """
    Setting up a test program for prerequisite requirements before writing unit tests.
    """

    # Setting up classes
    MATH21 = Course(code='MATH21', units=5, offered_quarters=[Quarter.FALL, Quarter.WINTER, Quarter.SPRING])
    MATH51 = Course(code='MATH51', units=5, offered_quarters=[Quarter.FALL, Quarter.WINTER, Quarter.SPRING], prereqs=[MATH21])
    MATH52 = Course(code='MATH52', units=5, offered_quarters=[Quarter.WINTER, Quarter.SPRING], prereqs=[MATH51])
    MATH56 = Course(code='MATH56', units=4, offered_quarters=[Quarter.FALL, Quarter.WINTER, Quarter.SPRING])
    MATH115 = Course(code='MATH115', units=4, offered_quarters=[Quarter.FALL, Quarter.WINTER, Quarter.SPRING], prereqs=[MATH51, MATH56])
    MATH151 = Course(code='MATH151', units=4, offered_quarters=[Quarter.WINTER], prereqs=[MATH52, MATH115])
    MATH136 = Course(code='MATH136', units=4, offered_quarters=[Quarter.FALL], prereqs=[MATH151])


    # Set up the degree program
    degreeProgram = Program(required_courses=[CS106B, CS109, CS229])

    constrainProfile = Profile


    """
    # Arranging constraint objects
    degreeProgram = Program(
        required_courses=[
            Course(code='C1', units=5, offered_quarters=[Quarter.FALL]),
            Course(code='C2', units=5, offered_quarters=[Quarter.WINTER]),
            Course(code='C3', units=5, offered_quarters=[Quarter.SPRING]),
            Course(code='C4', units=5, offered_quarters=[Quarter.SUMMER])
        ]
    )
    constrainProfile = Profile(max_quarter_units=5)

    # Creating and configuring solver
    scheduleSolver = SolverConfig(program=degreeProgram, profile=constrainProfile)
    scheduleSolver.add_required_courses_constraints()
    scheduleSolver.add_quarter_load_constraints()
    
    # Solving
    print(scheduleSolver.check_solvable())
    """

    
if __name__ == '__main__':
    main()