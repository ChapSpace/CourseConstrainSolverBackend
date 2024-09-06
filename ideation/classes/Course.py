class Course:
    
    def __init__(self, identifier: str, quarters_offered: list[str]) -> None:
        self.__identifier = identifier
        self.__quarters_offered = quarters_offered
        
    # To string
    def __str__(self):
        return f'{self.__identifier}'
    
    # Accessors
    def get_identifier(self):
        return self.__identifier
    def get_quarters_offered(self):
        return self.__quarters_offered
    
    
    