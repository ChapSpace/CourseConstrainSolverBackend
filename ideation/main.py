from classes.Course import Course
from classes.Program import Program
from classes.Quarters import Quarters
from z3 import *

def main():
    
    degreeProgram = Program([Course('C1',5, [Quarters['FRESH_FALL'].value, Quarters['FRESH_WINTER'].value]),
                            Course('C2', 5, [Quarters['FRESH_FALL'].value, Quarters['FRESH_SPRING'].value]),
                            Course('C3', 5, [Quarters['FRESH_WINTER'].value, Quarters['FRESH_SPRING'].value]),
                            Course('C4', 5, [Quarters['FRESH_WINTER'].value, Quarters['FRESH_FALL'].value]),
                            Course('C5', 5, [Quarters['FRESH_SPRING'].value, Quarters['FRESH_FALL'].value]),
                            Course('C6', 5, [Quarters['FRESH_SPRING'].value, Quarters['FRESH_WINTER'].value])])
    
    s = Solver()
    
    # Creating a dictionary of Int() z3 variables for subsequent access
    # Dynamically creating z3 Int() variables from degree program dict
    degreeCourses: dict[Int(): Course] = {}
    for course in degreeProgram.get_required_courses():
        degreeCourses[Int(course.get_name())] = course
    
    print(f"Course Dictionary: {degreeCourses}")
    
    # Dynamically adding the constraint that each class must be taken at least once
    for courseVar, course in degreeCourses.items():
        s.add(Or([courseVar == quarter for quarter in course.get_quarters()])) 
        
    # Dynamically adding the constraint that we can have no more than 2 classes per quarter
    for quarter in Quarters:
        load = sum([If(courseVar == quarter.value, 1, 0) for courseVar in degreeCourses])
        s.add(load <= 2)
    
    
    print(s.check())
    if (s.check() == sat):
        print(s.model())
   
    
if __name__ == "__main__":
    main()

