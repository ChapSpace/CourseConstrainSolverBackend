from classes.components.course import Course
from classes.constrain.program import Program
from classes.constrain.profile import Profile
from classes.components.enums import Quarter, GER, Grade, Grading

def test_course_from_dict_all_fields_populated():
    
    course = Course(
        code="CODE",
        title="TITLE",
        units=5,
        description="DESCRIPTION",
        prereqs=[Course(code="PREREQCODE", title="PREREQTITLE")],
        coreqs=[Course(code="COREQCODE", title="COREQTITLE")],
        offered_quarters=[Quarter.FRESH_FALL, Quarter.FRESH_WINTER],
        instructors=["INSTRUCTOR1", "INSTRUCTOR2"],
        median_hrs=15,
        median_grade=Grade.A_PLUS,
        percent_A_A_plus=100,
        ug_reqs=[GER.WAY_A_II, GER.WAY_AQR],
        grading=Grading.LETTER
    )
    
    course_dict = course.to_dict()
    
    course_from_dict = Course.from_dict(course_dict)
    
    assert course.code == course_from_dict.code
    assert course.title == course_from_dict.title
    assert course.units == course_from_dict.units
    assert course.description == course_from_dict.description
    # Prereqs
    # Coreqs
    assert course.offered_quarters == course_from_dict.offered_quarters
    assert course.instructors == course_from_dict.instructors
    assert course.median_hrs == course_from_dict.median_hrs
    assert course.median_grade == course_from_dict.median_grade
    assert course.percent_A_A_plus == course_from_dict.percent_A_A_plus
    assert course.ug_reqs == course_from_dict.ug_reqs
    assert course.grading == course_from_dict.grading