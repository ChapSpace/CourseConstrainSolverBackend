from classes.components.course import Course
from typing import List

class Program:
    
    def __init__(self, required_courses: List[Course]):
        self._required_courses = required_courses
    
    @property
    def required_courses(self) -> List[Course]:
        return self._required_courses
