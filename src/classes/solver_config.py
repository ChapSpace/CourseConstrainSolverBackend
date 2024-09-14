from z3 import *

from classes.constrain.program import Program
from classes.constrain.profile import Profile
from classes.components.course import Course
from classes.components.enums import Quarter

from collections import defaultdict
from typing import Dict, Set, List

class SolverConfig:
    """
    Configures the solver with required courses and constraints and generates a schedule.

    Attributes:
        solver (Solver): Z3 solver.
        program(Program): Degree program.
        profile(Profile): Student profile.
        course_dict(Dict[Int, Course]): Dictionary of course codes to course objects.
        prereq_graph(Dict[Int, Set[Int]]): Dictionary of course codes to prerequisite course codes.
        constraints(Dict[str, List[BoolExpr]]): Dictionary of constraint types to constraints.
        modifiers(Dict[str, Callable[[List[BoolExpr]], None]]): Dictionary of constraint types to modifier functions.
    """
    def __init__(
        self, 
        program: Program,
        profile: Profile = None,
    ) -> None:
        """Initializes the SolverConfig class."""
        self._solver = Solver()

        self._program = program
        self._profile = profile

        self._course_dict: Dict[Int, Course] = {}
        for course in self._program.required_courses:
            self._course_dict[Int(course.code)] = course

        self._prereq_graph = defaultdict(set)
        for course in self._program.required_courses:
            for prereq in course.prereqs:
                if Int(prereq.code) in self._course_dict:
                    self._prereq_graph[course.code].add(prereq.code)

        self._modifiers = {
            "max_quarter_units": self._max_quarter_units,
            "prerequisites": self._prerequisites,
            "required_courses": self._required_courses,
        }

        self.update()

    @property
    def course_dict(self) -> Dict[int, Course]:
        return self._course_dict

    @property
    def prereq_graph(self) -> Dict[int, Set[int]]:
        return self._prereq_graph
    
    @property
    def constraints(self) -> Dict[str, List[ExprRef]]:
        return self._constraints
    
    def get_assertions(self) -> List[ExprRef]:
        return self._solver.assertions()
    
    def check_solvable(self) -> CheckSatResult:
        return self._solver.check()
    
    def solve(self) -> Dict[str, Quarter] | None:
        """Solves the constraints and returns a schedule."""
        if self.check_solvable() == sat:
            model = self._solver.model()
            schedule = {}
            for course in self._program.required_courses:
                course_var = Int(course.code)
                quarter_val = model[course_var].as_long()
                quarter = Quarter(quarter_val)
                schedule[course.code] = quarter
            return schedule
        else:
            return None

    def update(self) -> None:
        """Updates the constraints."""
        self._solver.reset()
        for key, func in self._modifiers.items():
            func()
    
    def _max_quarter_units(self) -> None:
        """Adds max quarter units constraints to solver."""
        for quarter in Quarter:
            load = sum([If(courseVar == quarter.value, course.units, 0) for courseVar, course in self._course_dict.items()])
            constraint = load <= self._profile.max_quarter_units
            self._solver.add(constraint)

    def _min_quarter_units(self) -> None:
        """Adds min quarter units constraints to solver."""
        for quarter in Quarter:
            load = sum([If(courseVar == quarter.value, course.units, 0) for courseVar, course in self._course_dict.items()])
            constraint = load >= self._profile.min_quarter_units
            self._solver.add(constraint)

    def _prerequisites(self) -> None:
        """Adds prerequisite constraints to solver."""
        for course_code, prereqs in self._prereq_graph.items():
            course_var = Int(course_code)
            for prereq_code in prereqs:
                prereq_var = Int(prereq_code)
                self._solver.add(course_var > prereq_var)

    def _required_courses(self) -> None:
        """Adds required courses constraints to solver."""
        for courseVar, course in self._course_dict.items():
            constraint = Or([courseVar == quarter.value for quarter in course.offered_quarters])
            self._solver.add(constraint)