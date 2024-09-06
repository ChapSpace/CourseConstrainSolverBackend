from typing import List
from enums import Quarter
from enums import GER
from enums import Grade

"""
courses
code -> str
name -> str
units -> int | tuple(int, int)
description -> str
prereqs -> list(str)
offered terms -> list(Quarter)
instructors -> list(list(str))
median hrs -> int | float
median grade -> grade Enum | none
% A/A+ -> int | float | None
UG REQs -> GER enum
Grading -> Grading Enum

"""
class Course:
    def __init__(
            self, 
            code: str, 
            title: str,
            units: int | tuple[int, int],
            description: str,
            prereqs: list['Course'],
            coreqs: list['Course'],
            offered_terms: list[Quarter],
            instructors: list[list[str]],
            median_hrs: int | float,
            median_grade: Grade | None,
            percent_A_A_plus: int | float | None,
            ug_reqs: GER | None,
            grading: Grade | tuple[Grade, Grade]
    ) -> None:
        if isinstance(code, str):
            self.code = code
        else:
            raise TypeError(f"Code must be a str, but got {type(code).__name__}")

        if isinstance(title, str):
            self.title = title
        else:        
            raise TypeError(f"Title must be a str, but got {type(title).__name__}")
        
        if isinstance(units, int):
            self.units = units
        elif isinstance(units, (tuple, list)) and len(units) == 2:
            self.units = units
        else:
            raise TypeError(f"Units must be an int or tuple of two ints, but got {type(units).__name__}")
        
        if isinstance(description, str):
            self.description = description
        else:
            raise TypeError(f"Description must be a str, but got {type(description).__name__}")

    def __str__(self) -> str:
        pass

    def check_prereqs(self):
        pass

    def add_prereq(self) -> None:
        pass
