from classes.components.course import Course
from typing import List, Dict, Any

class Program:
    """Degree program with required courses."""
    def __init__(self, required_courses: List[Course]):
        self._required_courses = required_courses
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "required_courses": [course.to_dict() for course in self._required_courses]
        }
    
    
    @property
    def required_courses(self) -> List[Course]:
        return self._required_courses
