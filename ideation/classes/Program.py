class Program:
    
    def __init__(self, required_courses: list[str]) -> None:
        self.__required_courses = required_courses
        
    # Accessors
    def get_required_courses(self) -> list[str]:
        return self.__required_courses