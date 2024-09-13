from classes.constrain.program import Program
from classes.constrain.profile import Profile
from classes.components.course import Course
from classes.components.enums import Quarter

class MockDB:
    
    def __init__(self):
        
        # Setting up classes
        C1 = Course(code='C1', units=5, offered_quarters=[Quarter.FRESH_FALL])
        C2 = Course(code='C2', units=5, offered_quarters=[Quarter.FRESH_WINTER])
        C3 = Course(code='C3', units=5, offered_quarters=[Quarter.FRESH_SPRING])
        C4 = Course(code='C4', units=5, offered_quarters=[Quarter.FRESH_SUMMER])
        
        # Creating mock program and profiles
        self._program = Program(required_courses=[C1, C2, C3, C4])
        self._profile = Profile(max_quarter_units=20)
    
    @property
    def program(self):
        return self._program
    
    @property
    def profile(self):
        return self._profile