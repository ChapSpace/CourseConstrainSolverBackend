class Course:
    
    def __init__(self, name: str, units: int, quarters: list[int]) -> None:
        self.__name = name
        self.__units = units
        self.__quarters = quarters
        
    # To string
    def __str__(self):
        return f'{self.__name}'
    
    # Accessors
    def get_name(self):
        return self.__name
    def get_units(self):
        return self.__units
    def get_quarters(self):
        return self.__quarters
    
    
    