from z3 import *

from classes.constrain.program import Program
from classes.constrain.profile import Profile
from classes.components.course import Course
from classes.components.enums import Quarter

from collections import defaultdict
from typing import Dict, Set, List, Callable, BoolExpr

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
    def __init__():
        pass

    @property
    def course_dict(self) -> Dict[int, Course]:
        return self._course_dict

    @property
    def prereq_graph(self) -> Dict[int, Set[int]]:
        return self._prereq_graph
    
    @property
    def constraints(self) -> Dict[str, List[BoolExpr]]:
        return self._constraints
    
    def get_assertations(self):
        return self._solver.assertations()
    
    def solve(self):
        pass

    def _update(self, key: str) -> None:
        pass
    
    def _max_quarter_units(self):
        pass

    def _min_quarter_units(self):
        pass

    def _prerequisites(self):
        pass

    def _required_courses(self):
        pass