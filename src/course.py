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
            offered_quarters: list[Quarter],
            instructors: list[list[str]],
            median_hrs: int | float,
            median_grade: Grade | None,
            percent_A_A_plus: int | float | None,
            ug_reqs: list['GER'] | None,
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
        
        if isinstance(units, int) or (isinstance(units, tuple[int, int] and len(units) == 2)):
            self.units = units
        else:
            raise TypeError(f"Units must be an int or a tuple of two ints, but got {type(units).__name__}")
        
        if isinstance(description, str):
            self.description = description
        else:
            raise TypeError(f"Description must be a str, but got {type(description).__name__}")
        
        if isinstance(prereqs, list['Course']):
            self.prereqs = prereqs
        else:
            raise TypeError(f"Prereqs must be a list of Courses, but got {type(prereqs).__name__}")
        
        if isinstance(coreqs, list['Course']):        
            self.coreqs = coreqs
        else:
            raise TypeError(f"Coreqs must be a list of Courses, but got {type(coreqs).__name__}")
        
        if isinstance(offered_quarters, list[Quarter]):
            self.offered_quarters = offered_quarters
        else:
            raise TypeError(f"Offered quarters must be a list of Quarters, but got {type(offered_quarters).__name__}")
        
        if isinstance(instructors, list[list[str]]):
            self.instructors = instructors
        else:
            raise TypeError(f"Instructors must be a list of lists of str, but got {type(instructors).__name__}")
        
        if isinstance(median_hrs, int) or isinstance(median_hrs, float):
            self.median_hrs = median_hrs
        else:
            raise TypeError(f"Median hours must be an int or float, but got {type(median_hrs).__name__}")
        
        if isinstance(median_grade, Grade) or median_grade is None:
            self.median_grade = median_grade
        else:
            raise TypeError(f"Median grade must be a Grade Enum or None, but got {type(median_grade).__name__}")
        
        if isinstance(percent_A_A_plus, int) or isinstance(percent_A_A_plus, float) or percent_A_A_plus is None:
            self.percent_A_A_plus = percent_A_A_plus
        else:
            raise TypeError(f"Percent A/A+ must be an int, float, or None, but got {type(percent_A_A_plus).__name__}")
        
        if isinstance(ug_reqs, list['GER']) or ug_reqs is None:
            self.ug_reqs = ug_reqs
        else:
            raise TypeError(f"UG reqs must be a list of GER enums or None, but got {type(ug_reqs).__name__}")
        
        if isinstance(grading, Grade) or (isinstance(grading, tuple) and len(grading) == 2):
            self.grading = grading
        else:
            raise TypeError(f"Grading must be a Grade Enum or a tuple of two Grade Enums, but got {type(grading).__name__}")

    def __str__(self) -> str:
        pass

    def check_prereqs(self):
        pass

    def add_prereq(self) -> None:
        pass
