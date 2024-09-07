from typing import List, Optional, Union
from enums import Quarter, GER, Grade

class Course:
    """
    Represents a university course with various attributes like code, units, description, and grading.

    Attributes:
        code (str): The course code.
        title (str): The course title.
        units (int or tuple[int, int]): Course units.
        description (str): Course description.
        prereqs (List[Course]): List of prerequisite courses.
        coreqs (List[Course]): List of corequisite courses.
        offered_quarters (List[Quarter]): Quarters the course is offered.
        instructors (List[List[str]]): List of instructors per quarter.
        median_hrs (Union[int, float]): Median hours required.
        median_grade (Optional[Grade]): Median grade or None.
        percent_A_A_plus (Optional[Union[int, float]]): Percentage of A/A+ grades or None.
        ug_reqs (Optional[List[GER]]): Undergraduate requirements or None.
        grading (Union[Grade, Tuple[Grade, Grade]]): Grading scheme.
    """
    def __init__(
        self, 
        code: str, 
        title: str,
        units: Union[int, tuple[int, int]],
        description: str,
        prereqs: Optional[List['Course']] = None,
        coreqs: Optional[List['Course']] = None,
        offered_quarters: Optional[List[Quarter]] = None,
        instructors: Optional[List[List[str]]] = None,
        median_hrs: Union[int, float] = 0,
        median_grade: Optional[Grade] = None,
        percent_A_A_plus: Optional[Union[int, float]] = None,
        ug_reqs: Optional[List[GER]] = None,
        grading: Union[Grade, tuple[Grade, Grade]] = None
    ) -> None:
        self.code = code
        self.title = title
        self.units = units if isinstance(units, int) or (isinstance(units, tuple) and len(units) == 2) else None
        self.description = description
        self.prereqs = prereqs or []
        self.coreqs = coreqs or []
        self.offered_quarters = offered_quarters or []
        self.instructors = instructors or []
        self.median_hrs = median_hrs
        self.median_grade = median_grade
        self.percent_A_A_plus = percent_A_A_plus
        self.ug_reqs = ug_reqs
        self.grading = grading

    def __str__(self) -> str:
        return f"{self.code}: {self.title}"

    def get_prereqs(self):
        """Return the list of prerequisite courses."""
        return self.prereqs

    def add_prereq(self, prereq: 'Course') -> None:
        """Add a prerequisite to the course."""
        self.prereqs.append(prereq)
