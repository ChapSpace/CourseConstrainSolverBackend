from classes.components.course import Course
from classes.components.pool import Pool
from typing import List, Dict, Any

class Program:
    """
    Degree program with program requirements.
    
    Attributes:
        id (str): Describes the name of the program
        required_courses (List[Course]): The courses required to complete the program
        pools (List[Pool]): The pool requirements that must be satisfied to complete the program
    
    """
    def __init__(self, id: str, required_courses: List[Course], pools: List[Pool] = None):
        self._id = id
        self._required_courses = required_courses
        self._pools = pools
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "required_courses": [course.to_dict() for course in self._required_courses],
            "id": self._id,
            "pools": [pool.to_dict() for pool in self._pools]
        }
    
    @classmethod
    def from_dict(cls, dict) -> 'Program':
        return cls(
            required_courses=[Course.from_dict(course_dict) for course_dict in dict.get("required_courses")] if dict.get("required_courses") != None else [],
            id=dict.get("id"),
            pools=[Pool.from_dict(pool_dict) for pool_dict in dict.get("pools")] if dict.get("pools") != None else []
        )
    
    @property
    def id(self) -> str:
        return self._id
    @property
    def required_courses(self) -> List[Course]:
        return self._required_courses
    @property
    def pools(self) -> List[Pool]:
        return self._pools

