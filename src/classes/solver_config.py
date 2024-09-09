from z3 import *
from classes.constrain.program import Program
from classes.constrain.profile import Profile
from classes.components.course import Course
from classes.components.enums import Quarter
from typing import Dict

class SolverConfig:
    
    def __init__(self, 
                 program: Program, 
                 profile: Profile = None):
        
        self._program = program
        self._profile = profile
        
        self._solver = Solver()
        
        self._course_dict: Dict[Int, Course] = {}
        for course in self._program.required_courses:
            self._course_dict[Int(course.code)] = course
    
    # Solver
    def solve_constraints(self):
        res = self._solver.check()
        print(res)
        if res == sat:
            print(self._solver.model())
        
    # Add required courses to solver
    def add_required_courses_constraints(self):
        
        for courseVar, course in self._course_dict.items():
            self._solver.add(Or([courseVar == quarter.value for quarter in course.offered_quarters])) 
    
    # Add prerequisite constraints to solver
    def add_prerequisite_constraints(self):
        pass
        

    # Add quarter load constraints to solver
    def add_quarter_load_constraints(self):
        for quarter in Quarter:
            load = sum([If(courseVar == quarter.value, course.units, 0) for courseVar, course in self._course_dict.items()])
            self._solver.add(load <= self._profile.max_quarter_units)