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
    
    degreeCourses: dict[Int(): list[int]] = {}
    for course in degreeProgram.get_required_courses():
        degreeCourses[Int(course.get_name())] = course.get_quarters()
    print(degreeCourses)
    for key in degreeCourses:
        print(type(key))

main()
    
    

   
