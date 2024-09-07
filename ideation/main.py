from classes.Course import Course
from classes.Program import Program
from classes.Quarters import Quarters
from z3 import *

def main():
    
    degreeProgram = Program([Course('C1', [Quarters['FRESH_FALL'].value, Quarters['FRESH_WINTER'].value]),
                            Course('C2', [Quarters['FRESH_FALL'].value, Quarters['FRESH_SPRING'].value]),
                            Course('C3', [Quarters['FRESH_WINTER'].value, Quarters['FRESH_SPRING'].value]),
                            Course('C4', [Quarters['FRESH_WINTER'].value, Quarters['FRESH_FALL'].value]),
                            Course('C5', [Quarters['FRESH_SPRING'].value, Quarters['FRESH_FALL'].value]),
                            Course('C6', [Quarters['FRESH_SPRING'].value, Quarters['FRESH_WINTER'].value])])
    
    s = Solver()
    
    # Creating a dictionary of Int() z3 variables for subsequent access
    # Dynamically creating z3 Int() variables from degree program dict
    degreeCourses: dict[str: tuple(Int(), list[int])] = {}
    for course in degreeProgram.get_required_courses():
        degreeCourses[course.get_name()] = (Int(course.get_name()), course.get_quarters())
    
    print(degreeCourses)
    
    # Dynamically adding the constraint that each class must be taken at least once
    for courseVarKey in degreeCourses:
        courseVarPair = degreeCourses[courseVarKey]
        s.add(Or([courseVarPair[0] == quarter for quarter in courseVarPair[1]])) 
        
    # Dynamically adding the constraint that we can have no more than 2 classes per quarter
    for quarter in Quarters:
        load = sum([If(courseVarPair[0] == quarter.value, 1, 0) for courseVarPair in degreeCourses.values()])
        s.add(load <= 2)
    
    
    print(s.check())
    print(s.model())
   
    
if __name__ == "__main__":
    main()

