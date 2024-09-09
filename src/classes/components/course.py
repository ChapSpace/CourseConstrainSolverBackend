from typing import List, Optional, Union
from src.classes.components.enums import Quarter, GER, Grade

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
        code: str = None, 
        title: str = None,
        units: Union[int, tuple[int, int]] = None,
        description: str = None,
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
        self._code = code
        self._title = title
        self._units = units if isinstance(units, int) or (isinstance(units, tuple) and len(units) == 2) else None
        self._description = description
        self._prereqs = prereqs or []
        self._coreqs = coreqs or []
        self._offered_quarters = offered_quarters or []
        self._instructors = instructors or []
        self._median_hrs = median_hrs
        self._median_grade = median_grade
        self._percent_A_A_plus = percent_A_A_plus
        self._ug_reqs = ug_reqs
        self._grading = grading

    def __str__(self) -> str:
        return f"{self.code}: {self.title}"

    @property
    def code(self) -> str:
        return self._code
    
    @property
    def units(self) -> Union[int, tuple[int, int]]:
        """Return the course units."""
        return self._units
    
    @property
    def prereqs(self) -> List['Course']:
        """Return the list of prerequisite courses."""
        return self._prereqs
    
    def add_prereq(self, prereq: 'Course') -> None:
        """Add a prerequisite to the course."""
        if not isinstance(prereq, Course):
            raise TypeError(f"Prerequisite must be a 'Course' object, but got {type(prereq).__name__}")
        self._prereqs.append(prereq)

    @property
    def coreqs(self) -> List['Course']:
        """Return the list of corequisite courses."""
        return self._coreqs
    
    def add_coreq(self, coreq: 'Course') -> None:
        """Add a corequisite to the course."""
        if not isinstance(coreq, Course):
            raise TypeError(f"Corequisite must be a 'Course' object, but got {type(prereq).__name__}")
        self._coreqs.append(coreq)

    @property
    def offered_quarters(self) -> List[Quarter]:
        """Return the quarters the course is offered."""
        return self._offered_quarters
    
    @property
    def instructors(self) -> List[List[str]]:
        """Return the list of instructors per quarter."""
        return self._instructors
    
    @property
    def median_hrs(self) -> Union[int, float]:
        """Return the median hours required."""
        return self._median_hrs
    
    @property
    def median_grade(self) -> Optional[Grade]:
        """Return the median grade or None."""
        return self._median_grade
    
    @property
    def percent_A_A_plus(self) -> Optional[Union[int, float]]:
        """Return the percentage of A/A+ grades or None."""
        return self._percent_A_A_plus
    
    @property
    def ug_reqs(self) -> Optional[List[GER]]:
        """Return the undergraduate requirements or None."""
        return self._ug_reqs