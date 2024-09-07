from classes.Course import Course

class Program:
    
    def __init__(self, required_courses: list[Course]) -> None:
        self.__required_courses = required_courses
        
    # Accessors
    def get_required_courses(self) -> list[Course]:
        return self.__required_courses