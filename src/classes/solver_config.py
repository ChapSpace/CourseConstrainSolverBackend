from z3 import *
from classes.constrain.program import Program
from classes.constrain.profile import Profile
from classes.components.course import Course
from classes.components.enums import Quarter
from typing import Dict
from collections import defaultdict

class SolverConfig:
    """
    Configures the solver with required courses and constraints.

    Attributes:
        program (Program): Degree program.
        profile (Profile): Student profile.
        course_dict (Dict[Int, Course]): Dictionary of course codes to course objects.
        prereq_graph (Dict[Int, Set[Int]]): Dictionary of course codes to prerequisite course codes.
    """
    def __init__(
        self, 
        program: Program, 
        profile: Profile = None
    ) -> None:
        self._program = program
        self._profile = profile
        
        self._solver = Solver()
        
        self._course_dict: Dict[Int, Course] = {}
        for course in self._program.required_courses:
            self._course_dict[Int(course.code)] = course

        self._prereq_graph = defaultdict(set)
        for course in self._program.required_courses:
            for prereq in course.prereqs:
                if Int(prereq.code) in self._course_dict:
                    self._prereq_graph[course.code].add(prereq.code)

    @property
    def course_dict(self):
        return self._course_dict
    
    @property
    def prereq_graph(self):
        return self._prereq_graph

    # Returns if the problem is solvable
    def check_solvable(self):
        return self._solver.check()
        
    # Add required courses to solver
    def add_required_courses_constraints(self):
        for courseVar, course in self._course_dict.items():
            self._solver.add(Or([courseVar == quarter.value for quarter in course.offered_quarters])) 

    # Add prerequisite constraints to solver
    def add_prerequisite_constraints(self):
        for course_code, prereqs in self._prereq_graph.items():
            course_var = Int(course_code)
            for prereq_code in prereqs:
                prereq_var = Int(prereq_code)
                self._solver.add(course_var > prereq_var)

    # Add quarter load constraints to solver
    def add_quarter_load_constraints(self):
        for quarter in Quarter:
            load = sum([If(courseVar == quarter.value, course.units, 0) for courseVar, course in self._course_dict.items()])
            self._solver.add(load <= self._profile.max_quarter_units)

    def get_constraints(self):
        return self._solver.assertions()

    def solve(self):
        if self.check_solvable() == sat:
            model = self._solver.model()
            schedule = {}
            for course in self._program.required_courses:
                course_var = Int(course.code)
                quarter_value = model[course_var].as_long()
                quarter = Quarter(quarter_value)
                schedule[course.code] = quarter
            return schedule
        else:
            return None