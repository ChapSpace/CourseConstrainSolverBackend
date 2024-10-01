from classes.components.course import Course
from classes.constrain.program import Program
from classes.constrain.profile import Profile
from classes.components.enums import Quarter, GER, Grade, Grading
from classes.components.pool import Pool

def test_course_to_dict_all_fields_populated():
    
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
    
    expected_dict = {
        "code": "CODE",
        "title": "TITLE",
        "units": 5,
        "description": "DESCRIPTION",
        "prereqs": [
            {
                "code": "PREREQCODE",
                "title": "PREREQTITLE",
                "units": None,
                "description": None,
                "prereqs": [],
                "coreqs": [],
                "offered_quarters": [],
                "instructors": [],
                "median_hrs": None,
                "median_grade": None,
                "percent_A_A_plus": None,
                "ug_reqs": [],
                "grading": None
            }    
        ],
        "coreqs": [
            {
                "code": "COREQCODE",
                "title": "COREQTITLE",
                "units": None,
                "description": None,
                "prereqs": [],
                "coreqs": [],
                "offered_quarters": [],
                "instructors": [],
                "median_hrs": None,
                "median_grade": None,
                "percent_A_A_plus": None,
                "ug_reqs": [],
                "grading": None
            }
        ],
        "offered_quarters": ["FRESH_FALL", "FRESH_WINTER"],
        "instructors": ["INSTRUCTOR1", "INSTRUCTOR2"],
        "median_hrs": 15,
        "median_grade": "A_PLUS",
        "percent_A_A_plus": 100,
        "ug_reqs": ["WAY_A_II", "WAY_AQR"],
        "grading": "LETTER"
    }
    
    assert course_dict == expected_dict

def test_course_to_dict_optional_fields_empty():
    
    course = Course(code="CODE", title="TITLE")
    
    course_dict = course.to_dict()
    
    expected_dict = {
        "code": "CODE",
        "title": "TITLE",
        "units": None,
        "description": None,
        "prereqs": [],
        "coreqs": [],
        "offered_quarters": [],
        "instructors": [],
        "median_hrs": None,
        "median_grade": None,
        "percent_A_A_plus": None,
        "ug_reqs": [],
        "grading": None
    }
    
    assert course_dict == expected_dict
    
def test_program_to_dict():
    
    program = Program(
        id="ID",
        required_courses=[
            Course(
                code="CODE1",
                title="TITLE1",
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
            ),
            Course(
                code="CODE2",
                title="TITLE2",
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
        ],
        pools=[
            Pool(
                type="Course",
                objects=["C1", "C2", "C3"],
                num_required=2
            ),
            Pool(
                type="Pool",
                objects=[
                    Pool(
                        type="Course",
                        objects=["C4", "C5", "C6"],
                        num_required=2
                    ),
                    Pool(
                        type="Course",
                        objects=["C7", "C8", "C9"],
                        num_required=2
                    )
                ],
                num_required=1
            )
        ]
    )
    
    program_dict = program.to_dict()
    
    expected_dict = {
        "id": "ID",
        "required_courses": [
            {
                "code": "CODE1",
                "title": "TITLE1",
                "units": 5,
                "description": "DESCRIPTION",
                "prereqs": [
                    {
                        "code": "PREREQCODE",
                        "title": "PREREQTITLE",
                        "units": None,
                        "description": None,
                        "prereqs": [],
                        "coreqs": [],
                        "offered_quarters": [],
                        "instructors": [],
                        "median_hrs": None,
                        "median_grade": None,
                        "percent_A_A_plus": None,
                        "ug_reqs": [],
                        "grading": None
                    }    
                ],
                "coreqs": [
                    {
                        "code": "COREQCODE",
                        "title": "COREQTITLE",
                        "units": None,
                        "description": None,
                        "prereqs": [],
                        "coreqs": [],
                        "offered_quarters": [],
                        "instructors": [],
                        "median_hrs": None,
                        "median_grade": None,
                        "percent_A_A_plus": None,
                        "ug_reqs": [],
                        "grading": None
                    }
                ],
                "offered_quarters": ["FRESH_FALL", "FRESH_WINTER"],
                "instructors": ["INSTRUCTOR1", "INSTRUCTOR2"],
                "median_hrs": 15,
                "median_grade": "A_PLUS",
                "percent_A_A_plus": 100,
                "ug_reqs": ["WAY_A_II", "WAY_AQR"],
                "grading": "LETTER"
            },
            {
                "code": "CODE2",
                "title": "TITLE2",
                "units": 5,
                "description": "DESCRIPTION",
                "prereqs": [
                    {
                        "code": "PREREQCODE",
                        "title": "PREREQTITLE",
                        "units": None,
                        "description": None,
                        "prereqs": [],
                        "coreqs": [],
                        "offered_quarters": [],
                        "instructors": [],
                        "median_hrs": None,
                        "median_grade": None,
                        "percent_A_A_plus": None,
                        "ug_reqs": [],
                        "grading": None
                    }    
                ],
                "coreqs": [
                    {
                        "code": "COREQCODE",
                        "title": "COREQTITLE",
                        "units": None,
                        "description": None,
                        "prereqs": [],
                        "coreqs": [],
                        "offered_quarters": [],
                        "instructors": [],
                        "median_hrs": None,
                        "median_grade": None,
                        "percent_A_A_plus": None,
                        "ug_reqs": [],
                        "grading": None
                    }
                ],
                "offered_quarters": ["FRESH_FALL", "FRESH_WINTER"],
                "instructors": ["INSTRUCTOR1", "INSTRUCTOR2"],
                "median_hrs": 15,
                "median_grade": "A_PLUS",
                "percent_A_A_plus": 100,
                "ug_reqs": ["WAY_A_II", "WAY_AQR"],
                "grading": "LETTER"
            },
        ],
        "pools": [
            {
                "type": "Course",
                "objects": ["C1", "C2", "C3"],
                "num_required": 2
            },
            {
                "type": "Pool",
                "objects": [
                    {
                        "type": "Course",
                        "objects": ["C4", "C5", "C6"],
                        "num_required": 2
                    },
                    {
                        "type": "Course",
                        "objects": ["C7", "C8", "C9"],
                        "num_required": 2
                    }
                ],
                "num_required": 1
            }
        ]
    }
    
    assert program_dict == expected_dict
    
def test_profile_to_dict():
    
    profile = Profile(id="ID", max_quarter_units=20, min_quarter_units=12)
    
    profile_dict = profile.to_dict()
    
    expected_dict = {
        "id": "ID",
        "max_quarter_units": 20,
        "min_quarter_units": 12
    }
    
    assert profile_dict == expected_dict

def test_course_pool_to_dict():
    
    course_pool = Pool(type="Course", objects=["C1", "C2", "C3"], num_required=2)
    
    course_pool_dict = course_pool.to_dict()
    
    expected_dict ={
        "type": "Course",
        "objects": ["C1", "C2", "C3"],
        "num_required": 2
    }
    
    assert course_pool_dict == expected_dict
    
def test_pool_pool_to_dict():
    
    pool_pool = Pool(
        type="Pool",
        objects=[
            Pool(
                type="Course",
                objects=["C1", "C2", "C3"],
                num_required=2
            ),
            Pool(
                type="Course",
                objects=["C4", "C5", "C6"],
                num_required=1
            )
        ],
        num_required=1
    )
    
    pool_pool_dict = pool_pool.to_dict()
    
    expected_dict = {
        "type": "Pool",
        "objects": [
            {
                "type": "Course",
                "objects": ["C1", "C2", "C3"],
                "num_required": 2
            },
            {
                "type": "Course",
                "objects": ["C4", "C5", "C6"],
                "num_required": 1
            }
        ],
        "num_required": 1
    }
    
    
    
     
    