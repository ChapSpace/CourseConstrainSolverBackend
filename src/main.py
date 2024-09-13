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
    C1 = Course(code='C1', units=5, offered_quarters=[Quarter.FRESH_FALL, Quarter.FRESH_WINTER])
    C2 = Course(code='C2', units=5, offered_quarters=[Quarter.FRESH_FALL, Quarter.FRESH_WINTER])
    C3 = Course(code='C3', units=5, offered_quarters=[Quarter.FRESH_FALL, Quarter.FRESH_WINTER, Quarter.FRESH_SPRING], prereqs=[C1, C2])
    C4 = Course(code='C4', units=5, offered_quarters=[Quarter.FRESH_SPRING], prereqs=[C3])

    # Setting up constraint objects
    degreeProgram = Program(required_courses=[C1, C2, C3, C4])
    constrainProfile = Profile(max_quarter_units=20)

    # Creating and configuring solver
    scheduleSolver = SolverConfig(program=degreeProgram, profile=constrainProfile)
    scheduleSolver.add_required_courses_constraints()
    scheduleSolver.add_prerequisite_constraints()
    scheduleSolver.add_quarter_load_constraints()

    #print(scheduleSolver.prereq_graph)

    print(scheduleSolver.get_constraints())

    print(scheduleSolver.check_solvable())

    schedule = scheduleSolver.solve()

    if schedule:
        for course_code, quarter in schedule.items():
            print(f"{course_code} is scheduled for {quarter}")
    else:
        print("No valid schedule found")

    
if __name__ == '__main__':
    main()