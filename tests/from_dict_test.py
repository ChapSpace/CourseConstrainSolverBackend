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
    
    assert type(course_from_dict) == Course
    assert course.code == course_from_dict.code
    assert course.title == course_from_dict.title
    assert course.units == course_from_dict.units
    assert course.description == course_from_dict.description
    # Add prereqs checking
    # Add coreqs checking
    assert course.offered_quarters == course_from_dict.offered_quarters
    assert course.instructors == course_from_dict.instructors
    assert course.median_hrs == course_from_dict.median_hrs
    assert course.median_grade == course_from_dict.median_grade
    assert course.percent_A_A_plus == course_from_dict.percent_A_A_plus
    assert course.ug_reqs == course_from_dict.ug_reqs
    assert course.grading == course_from_dict.grading

def test_course_from_dict_some_field_unpopulated():
    
    course = Course(
        code="CODE",
        title="TITLE"
    )
    
    course_dict = course.to_dict()
    
    course_from_dict = Course.from_dict(course_dict)
    
    assert type(course_from_dict) == Course
    assert course.code == course_from_dict.code
    assert course.title == course_from_dict.title

def test_program_from_dict():
    
    program = Program(
        name="NAME",
        required_courses=[
            Course(code="C1", title="Course 1"),
            Course(code="C2", title="Course 2")
        ]
    )
    
    program_dict = program.to_dict()
    
    program_from_dict = Program.from_dict(program_dict)
    
    assert type(program_from_dict) == Program
    assert program.name == program_from_dict.name
    assert program.required_courses[0].code == program_from_dict.required_courses[0].code
    assert program.required_courses[0].title == program_from_dict.required_courses[0].title
    assert program.required_courses[1].code == program_from_dict.required_courses[1].code
    assert program.required_courses[1].title == program_from_dict.required_courses[1].title

def test_profile_from_dict():
    
    profile = Profile(
        max_quarter_units=20,
        min_quarter_units=12
    )
    
    profile_dict = profile.to_dict()
    
    profile_from_dict = Profile.from_dict(profile_dict)
    
    assert type(profile_from_dict) == Profile
    assert profile.max_quarter_units == profile_from_dict.max_quarter_units
    assert profile.min_quarter_units == profile_from_dict.min_quarter_units