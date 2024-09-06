class Course:
    __init__(
            self, 
            code: str, 
            name: str,
            units: int | tuple[int, int]
    ) -> None:
        if not isinstance(code, str):
          raise TypeError(f"Code must be a str, but got {type(code).__name__}")
        if not isinstance(name, str):
            raise TypeError(f"Name must be a str, but got {type(name).__name__}")
        if not isinstance(units, int) or not (isinstance(units, (tuple, list)) and len(units) == 2):
            raise TypeError(f"Units must be an int or tuple of two ints, but got {type(units).__name__}")
    
        self.code = code
        self.name = name
        self.units = units

    __str__(self):
        pass
