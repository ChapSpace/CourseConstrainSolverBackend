from classes.components.course import Course
from typing import List, Dict, Any

class Program:
    """Degree program with required courses."""
    def __init__(self, name: str, required_courses: List[Course]):
        self._required_courses = required_courses
        self._name = name
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "required_courses": [course.to_dict() for course in self._required_courses],
            "name": self._name
        }
    
    @classmethod
    def from_dict(cls, dict) -> 'Program':
        return cls(
            required_courses=[Course.from_dict(course_dict) for course_dict in dict.get("required_courses")],
            name=dict.get("name")
        )
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def required_courses(self) -> List[Course]:
        return self._required_courses

